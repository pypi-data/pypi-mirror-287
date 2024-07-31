#!/usr/bin/env python

"""
This module allows usage of the autct API to:
* create AUTCT proofs
* ask for verification (to receive tokens/services/etc.) from a server,
of an existing proof
* create taproot keys/addresses

.. and all of this can be done without any crypto libraries
in your Python application.
The RPC API calls are made over websockets, which AUTCT supports.
see github.com/AdamISZ/aut-ct for explanation of what AUTCT is.
"""

import json
import asyncio
import websockets
from websockets import client
from dataclasses import dataclass, asdict


RPC_PROOF_ERRORCODES = {0: "Success.",
                        -1:"Undefined failure in proving.",
                        -2: "Proving request rejected, must be only one context:keyset provided.",
                        -3: "Proving request rejected, provided context label is not served.",
                        -4: "Proving request rejected, provided keyset is not served.",
                        -5: "Proving request rejected, wrong bitcoin network.",
                        -6: "Proving request rejected, could not read private key from file.",
                        -7: "Proving request rejected, invalid private key format (must be WIF or hex).",
                        -8: "Proving request rejected, provided key is not in the keyset"}

RPC_VERIFY_ERRORCODES = {1: "Request was accepted by the Autct verifier! The proof is valid and the (unknown) pubkey is unused.",
                        -1: "Request rejected, PedDLEQ proof does not match the tree.",
                        -2: "Request rejected, PedDLEQ proof is invalid.",
                        -3: "Request rejected, proofs are valid but key image is reused.",
                        -4: "Request rejected, keyset chosen does not match the server's."}

RPC_CREATEKEYS_ERRORCODES = {0: "New key and address generated successfully",
                             -1: "Undefined failure in key generation.",
                             -2: "New key request rejected, mismatch in bitcoin network.",
                             -3: "New key request rejected, could not write private key to specified file location."}

@dataclass(unsafe_hash=True)
class AutctConfig:
    '''Replicates configuration of autct;
       note we do not include 'mode' as it is
       only used for CLI.'''
    keysets: str = 'my-context:testdata/fakekeys-6.txt'
    user_string: str = 'name-goes-here'
    depth: int = 2
    branching_factor: int = 1024
    generators_length_log_2: int = 11
    rpc_host: str = '127.0.0.1'
    rpc_port: int = 23333
    proof_file_str: str = 'default-proof-file'
    privkey_file_str: str = 'privkey'
    keyimage_filename_suffix: str = 'keyimages'
    base64_proof: bool = False
    bc_network: str = 'signet'

    def config_to_proof_req(self):
        return {"keyset":self.keysets,
                "depth":self.depth,
                "generators_length_log_2":self.generators_length_log_2,
                "user_label":self.user_string,
                "key_credential":self.privkey_file_str,
                "bc_network":self.bc_network}

    def config_to_verify_req(self, proof):
        return {"keyset":self.keysets,
                "user_label":self.user_string,
                "context_label":"my-context", #TODO; is this ignored in server?
                "application_label":"autct-v1.0",
                "proof":proof}

    def config_to_createkeys_request(self):
        return {"bc_network": self.bc_network,
                "privkey_file_loc": self.privkey_file_str}

def get_websocket_uri(host: str, port: int=-1, ssl: bool=False):
    header = "wss" if ssl else "ws"
    portstr = "" if port == -1 else str(port)
    return header + "://" + host + ":" + portstr

async def rpc_request(config_obj: dict, rpc_method_name: str, rpc_request_body: dict):
    ws_uri = get_websocket_uri(config_obj["rpc_host"], config_obj["rpc_port"])
    async with websockets.connect(ws_uri) as websocket:
        aclient = AutctWSRPCClient(websocket)
        return await aclient.make_request(rpc_method_name, rpc_request_body)
    
class AutctWSRPCClient:
    reqnum = 0
    def __init__(self, websocket: client.WebSocketClientProtocol, debug: bool=False):
        self.debug = debug
        self.websocket = websocket

    async def make_request(self, rpc_name: str, rpc_object: dict):
        # To request, we need two sends, first is:
        # "id": num, "service_method": method name, "timeout": (some seconds)
        # then *without waiting for a response*:
        # then send: the jsonified body of the request object with all fields.
        # Note the usage of binary, not text, encoding.
        await self.websocket.send(b'{"Request": {"id": ' + \
            str(self.reqnum).encode() + b', "service_method": "' + \
            rpc_name.encode() + b'","timeout": {"secs": 120,"nanos": 0}}}\n')
        await self.websocket.send(json.dumps(rpc_object).encode())

        # Then to receive the response, we need two recv() calls:
        # First is really an Acknowledgement or some such like:
        # b'{"Response":{"id":num,"is_ok":true}}\n' 
        # Second, call recv() again and get the jsonified Response object with all fields.        
        # TODO: handling of a NACK?
        result1 = await self.websocket.recv()
        if self.debug:
            print("Received ack receipt for our RPC request: {}".format(result1))
        result2 = await self.websocket.recv()
        if self.debug:
            print("Received raw response to our RPC request: {}".format(result2))
        return json.loads(result2.decode())

""" THE REMAINING CODE IS TO ILLUSTRATE USAGE OF THE API:
"""

async def run_all_requests_example():
    # The following examples illustrate correct usage of the API in its 3 calls:
    # 1. "prove" - for which you need to provide the file location of the
    #    relevant private key; the proof will be returned in base64.
    # 2. "verify" - for which you need to pass in the proof in base64.
    # 3. "createkeys" - will store a new private key in a file and give the
    #    corresponding taproot address.

    # First, create a default config set:
    config = AutctConfig()

    # parameters for "prove":
    # this is just an example; the private key 040404... stored in a file
    config.privkey_file_str = "privkey-four"
    # whereever you want to store the proof; note that relative paths are
    # for the server.
    config.proof_file_str = "test-proof-file"
    proving_request = config.config_to_proof_req()
    proving_result = await rpc_request(asdict(config), "RPCProver.prove", proving_request)
    if proving_result["accepted"] == 0:
        print("Proving request successful!")
    else:
        if proving_result["accepted"] not in RPC_PROOF_ERRORCODES:
            print("Unrecognized error code from server!: {}".format(proving_result["accepted"]))
        else:
            print("Proving failed due to error: \n{}".format(RPC_PROOF_ERRORCODES[proving_result["accepted"]]))

    print("\nNow we try verifying the proof that we just created:\n")
    # for the verification, we pass the proof in base64 in a field in the request;
    # we don't take it directly from a file:
    verifying_req = config.config_to_verify_req(proving_result["proof"])
    verifying_result = await rpc_request(asdict(config), "RPCProofVerifier.verify", verifying_req)
    if verifying_result["accepted"] not in RPC_VERIFY_ERRORCODES:
        print("Unrecognized error code from server!: {}".format(verifying_result["accepted"]))
    else:    
        print("Server response: \n{}".format(RPC_VERIFY_ERRORCODES[verifying_result["accepted"]]))

    # lastly we create a new key and taproot address; specify a file location for the private key:
    config.privkey_file_str = "new-privkey"
    createkeys_request = config.config_to_createkeys_request()
    createkeys_result = await rpc_request(asdict(config), "RPCCreateKeys.createkeys", createkeys_request)
    print("Server response: \n{}".format(RPC_CREATEKEYS_ERRORCODES[createkeys_result["accepted"]]))
    if createkeys_result["accepted"] == 0:
        print("The server generated this address: {}, and stored the corresponding private key in {}".format(createkeys_result["address"], createkeys_result["privkey_file_loc"]))

# Just run the sample requests if this file is executed:
asyncio.run(run_all_requests_example())
   
                     
                        

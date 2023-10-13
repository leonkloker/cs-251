from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cTZM84Q2QifgwS4E1q7KKfBaMPgLhy3CurR3GEpVRdyPUk84SJG9')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cPAJUCZZccHBFGBjhKWzeBRg7hp1KTBgyNMtRPAteabmJrjngmQ8')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cPnmBxiencMuQgcTQKLPtgNbHBnhDsYWY2zAyLJiuXBbA3M7GJ9y')
cust3_public_key = cust3_private_key.pub

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
    my_public_key, OP_CHECKSIGVERIFY, 1, cust1_public_key, cust2_public_key, 
    cust3_public_key, 3, OP_CHECKMULTISIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '2fcc5dea45cde3d291b7525771065f63fb512b00dc6b016290e1b5187631e235')
    utxo_index = 4 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

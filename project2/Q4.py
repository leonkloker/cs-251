from bitcoin.core.script import *

######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# TODO: Fill these in to create scripts that are redeemable by both
#       of the above conditions.
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        OP_IF, OP_HASH160, hash_of_secret, OP_EQUALVERIFY, OP_ELSE, public_key_sender,
        OP_CHECKSIGVERIFY, OP_ENDIF, public_key_recipient, OP_CHECKSIG
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        sig_recipient, secret, OP_TRUE
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        sig_recipient, sig_sender, OP_FALSE
    ]
######################################################################

######################################################################
#
# Configured for your addresses
#
# TODO: Fill in all of these fields
#

alice_txid_to_spend     = "ae7a8b1b8d5df61f59a09c8fd3e31bb46b593cd7794b1bd4f45d6c6099ad923b"
alice_utxo_index        = 0
alice_amount_to_send    = 0.00001

bob_txid_to_spend       = "a4b35e94b83d7b7e9b05a3089a41927911532e86837889dccd6dac95444bb185"
bob_utxo_index          = 0
bob_amount_to_send      = 0.00001

# Get current block height (for locktime) in 'height' parameter for each blockchain (will be used in swap.py):
#  curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height  = 2532719

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height   = 1022176

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
# alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.00001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = False

######################################################################

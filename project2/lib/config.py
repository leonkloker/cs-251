from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://testnet-faucet.mempool.co/

my_private_key = CBitcoinSecret(
    'cUP3Dq9ewGwsVaLPTYpm8zZMRrfwcReTMCg6XqKX5WBvJLZsT74J')

my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################
# faucet transaction hash ef6716dfeb8a34e0ba504207a3cd644623a563b7345c1f838ea295cccf7813f5
# split to 9 transaction hash 2fcc5dea45cde3d291b7525771065f63fb512b00dc6b016290e1b5187631e235

######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://testnet-faucet.mempool.co/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cQZCAZcqwtmyf4Q7RzHRqAxk4MCMf8XnZg3aGbLaLL1qcnu4Hy6v')
# transaction ae7a8b1b8d5df61f59a09c8fd3e31bb46b593cd7794b1bd4f45d6c6099ad923b
# split transaction 

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cUL4zb4uVSPGyt98HSjAu1jFf5eaWqjZDoWQbBVsyNrqa6FLikfB')

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=YOURTOKEN
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('6b1bc3d26a9d229578e9ac4a562337a6f2a594e4d40dc021a9391c66ec4edf65'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('f3c1135420b213145ed1339f8fc66d3b62546b325bd0da6e67d74142bc5ffd2d'))

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################
# transaction hash 15980834644bc7cdf4bb6789976da304cd91c12a0c0cb602f57df1f7bca7d1ee
# split hash a4b35e94b83d7b7e9b05a3089a41927911532e86837889dccd6dac95444bb185

from pathlib import Path

from genlayer_py import (
    create_client,
    create_account,
    localnet
)

import time


client = create_client(
    chain=localnet,
    endpoint="http://localhost:4000/api"
)

account = create_account()

client.local_account = account

print("Account:", account.address)

contract_path = Path(
    "icontracts/negotiation_contract.py"
)

with open(contract_path, "r") as f:

    contract_code = f.read()

print("Deploying contract...")

tx_hash = client.deploy_contract(
    code=contract_code,
    args=[]
)

print("TX HASH:", tx_hash)

receipt = client.w3.eth.wait_for_transaction_receipt(
    tx_hash
)

print("RECEIPT:", receipt)

time.sleep(5)

print("Contract deployed successfully.")

from genlayer_py import (
    create_client,
    create_account,
    localnet
)

client = create_client(
    chain=localnet,
    endpoint="http://localhost:4000/api"
)

account = create_account()

client.local_account = account

CONTRACT_ADDRESS = "0xA3364EA300FB74B4b7F64A4303a7ba0ab9686F0d"

print("Calling contract...")

tx_hash = client.write_contract(
    address=CONTRACT_ADDRESS,
    function_name="create_agreement",
    args=[
        "deal_1",
        "buyer_agent",
        "seller_agent",
        200,
        24
    ]
)

print("TX HASH:", tx_hash)

receipt = client.w3.eth.wait_for_transaction_receipt(
    tx_hash
)

print("RECEIPT:", receipt)

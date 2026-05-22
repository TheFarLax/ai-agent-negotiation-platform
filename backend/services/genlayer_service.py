import uuid

from genlayer_py import (
    create_client,
    create_account,
    localnet
)

from contract_config import CONTRACT_ADDRESS

from contracts.negotiation_contract import (
    NegotiationContract
)


client = create_client(
    chain=localnet,
    endpoint="http://localhost:4000/api"
)

account = create_account()

client.local_account = account

contract = NegotiationContract()


def store_on_genlayer(agreement):

    agreement_id = str(uuid.uuid4())

    tx_hash = client.write_contract(

        address=CONTRACT_ADDRESS,

        function_name="create_agreement",

        args=[
            agreement_id,
            "buyer_agent",
            "seller_agent",
            agreement["price"],
            agreement["deadline_hours"]
        ]
    )

    receipt = client.w3.eth.wait_for_transaction_receipt(
        tx_hash
    )

    return {

        "agreement_id": agreement_id,

        "tx_hash": tx_hash,

        "status": receipt.status
    }


def submit_validator_result(
    agreement_id,
    validator_result
):

    result = contract.submit_validator_vote(
        agreement_id=agreement_id,
        approved=validator_result["approved"],
        reason=validator_result["reason"]
    )

    return result


def submit_appeal_result(
    agreement_id,
    validator_result
):

    result = contract.submit_appeal_vote(
        agreement_id=agreement_id,
        approved=validator_result["approved"],
        reason=validator_result["reason"]
    )

    return result

escrow_accounts = {}


def create_escrow(agreement_id, amount):

    escrow_accounts[agreement_id] = {
        "amount": amount,
        "released": False
    }

    return {
        "status": "escrow_created",
        "agreement_id": agreement_id,
        "amount": amount
    }


def release_escrow(agreement_id):

    if agreement_id not in escrow_accounts:

        return {
            "status": "error",
            "message": "Agreement not found"
        }

    escrow_accounts[agreement_id]["released"] = True

    return {
        "status": "payment_released",
        "agreement_id": agreement_id,
        "amount": escrow_accounts[agreement_id]["amount"]
    }

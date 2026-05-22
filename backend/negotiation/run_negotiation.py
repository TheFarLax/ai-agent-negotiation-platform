import json

from agents.buyer_agent import buyer_agent
from agents.seller_agent import seller_agent


def run_negotiation(user_request):

    buyer_offer = None
    seller_offer = None

    history = []

    rounds = 5

    for i in range(rounds):

        seller_offer = seller_agent(
            user_request,
            {
                "buyer_offer": buyer_offer,
                "history": history
            }
        )

        seller_data = json.loads(seller_offer)

        history.append({
            "role": "seller",
            "offer": seller_data
        })

        if seller_data["accepted"]:

            return {
                "history": history,
                "final_agreement": seller_data
            }

        buyer_offer = buyer_agent(
            user_request,
            {
                "seller_offer": seller_offer,
                "history": history
            }
        )

        buyer_data = json.loads(buyer_offer)

        history.append({
            "role": "buyer",
            "offer": buyer_data
        })

        if buyer_data["accepted"]:

            return {
                "history": history,
                "final_agreement": buyer_data
            }

    return {
        "history": history,
        "final_agreement": {
            "message": "No agreement reached",
            "price": 0,
            "deadline_hours": 0,
            "accepted": False
        }
    }

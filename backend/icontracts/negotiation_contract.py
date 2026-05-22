class NegotiationContract:

    def __init__(self):

        self.agreements = {}

    def create_agreement(
        self,
        agreement_id,
        buyer,
        seller,
        price,
        deadline_hours
    ):

        self.agreements[agreement_id] = {

            "buyer": buyer,
            "seller": seller,
            "price": price,
            "deadline_hours": deadline_hours,
            "approved": False,
            "payment_released": False
        }

        return {
            "status": "agreement_created",
            "agreement_id": agreement_id
        }

    def approve_delivery(self, agreement_id):

        self.agreements[agreement_id][
            "approved"
        ] = True

        return {
            "status": "approved"
        }

    def release_payment(self, agreement_id):

        self.agreements[agreement_id][
            "payment_released"
        ] = True

        return {
            "status": "payment_released"
        }

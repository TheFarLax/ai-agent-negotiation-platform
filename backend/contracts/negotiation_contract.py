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
            "payment_released": False,

            "validator_votes": [],

            "appealed": False,
            "appeal_votes": []
        }

        return {
            "status": "agreement_created",
            "agreement_id": agreement_id
        }

    def submit_validator_vote(
        self,
        agreement_id,
        approved,
        reason
    ):

        self.agreements[agreement_id][
            "validator_votes"
        ].append({
            "approved": approved,
            "reason": reason
        })

        votes = self.agreements[agreement_id][
            "validator_votes"
        ]

        approvals = sum(
            1 for v in votes if v["approved"]
        )

        rejections = len(votes) - approvals

        if approvals >= 2:

            self.agreements[agreement_id][
                "approved"
            ] = True

            return {
                "consensus": "approved",
                "votes": votes
            }

        if rejections >= 2:

            return {
                "consensus": "rejected",
                "votes": votes
            }

        return {
            "consensus": "pending",
            "votes": votes
        }

    def submit_appeal_vote(
        self,
        agreement_id,
        approved,
        reason
    ):

        self.agreements[agreement_id][
            "appealed"
        ] = True

        self.agreements[agreement_id][
            "appeal_votes"
        ].append({
            "approved": approved,
            "reason": reason
        })

        votes = self.agreements[agreement_id][
            "appeal_votes"
        ]

        approvals = sum(
            1 for v in votes if v["approved"]
        )

        rejections = len(votes) - approvals

        if approvals >= 3:

            self.agreements[agreement_id][
                "approved"
            ] = True

            return {
                "appeal_consensus": "approved",
                "votes": votes
            }

        if rejections >= 3:

            return {
                "appeal_consensus": "rejected",
                "votes": votes
            }

        return {
            "appeal_consensus": "pending",
            "votes": votes
        }

    def release_payment(self, agreement_id):

        if agreement_id not in self.agreements:

            return {
                "status": "error",
                "message": "Agreement not found"
            }

        if not self.agreements[agreement_id]["approved"]:

            return {
                "status": "cannot_release",
                "message": "Agreement not approved"
            }

        self.agreements[agreement_id][
            "payment_released"
        ] = True

        return {
            "status": "payment_released",
            "agreement_id": agreement_id,
            "amount": self.agreements[agreement_id]["price"]
        }

    def get_agreement(self, agreement_id):

        if agreement_id not in self.agreements:

            return {
                "status": "error",
                "message": "Agreement not found"
            }

        return self.agreements[agreement_id]

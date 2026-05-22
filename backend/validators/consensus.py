from validators.delivery_validator import evaluate_delivery


def run_consensus(task, agreement, delivery):

    results = []

    for i in range(3):

        result = evaluate_delivery(
            task,
            agreement,
            delivery
        )

        results.append(result)

    approvals = sum(
        1 for r in results if r["approved"]
    )

    rejected = len(results) - approvals

    final_decision = approvals > rejected

    return {
        "final_approved": final_decision,
        "validator_results": results,
        "consensus": f"{approvals}/3 validators approved"
    }

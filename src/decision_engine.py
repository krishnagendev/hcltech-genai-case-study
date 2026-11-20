
def evaluate_claim(claim, tool_results):

    receipt = tool_results["receipt"]
    limits = tool_results["limits"]
    duplicates = tool_results["duplicates"]
    approval = tool_results["approval"]

    claimed = sum(
        float(item.get("amount", 0))
        for item in claim.get("expenses", [])
    )

    allowed = limits["calculated_allowed"]
    deducted = limits["calculated_deducted"]

    # Extract missing documents
    missing_docs = receipt.get("missing_receipts", [])

    # Collect policy references
    policy_refs = []

    if missing_docs:
        policy_refs.append("POL-RCT-01")

    if deducted > 0:
        policy_refs.append("POL-PD-01")

    if duplicates["duplicate_found"]:
        policy_refs.append("POL-DUP-01")

    if approval["manual_review"]:
        policy_refs.append("POL-APR-01")

    # Decision logic
    if (
        missing_docs
        or duplicates["duplicate_found"]
        or approval["manual_review"]
    ):
        decision = "MANUAL_REVIEW"
        approved_amount = 0
        deducted_amount = 0

    elif allowed == 0:
        decision = "REJECT"
        approved_amount = 0
        deducted_amount = claimed

    elif deducted > 0:
        decision = "PARTIAL_APPROVE"
        approved_amount = allowed
        deducted_amount = deducted

    else:
        decision = "APPROVE"
        approved_amount = allowed
        deducted_amount = 0

    # Explanation
    explanation = (
        f"Claim {claim['claim_id']} evaluated successfully. "
        f"Claimed amount: {claimed:.2f} USD. "
        f"Eligible amount: {allowed:.2f} USD. "
        f"Decision: {decision}."
    )

    return {
        "claim_id": claim["claim_id"],
        "decision": decision,
        "approved_amount": round(approved_amount, 2),
        "deducted_amount": round(deducted_amount, 2),
        "missing_docs": missing_docs,
        "policy_refs": list(set(policy_refs)),
        "confidence": 0.95,
        "explanation": explanation,
        "tools_used": list(tool_results.keys())
    }

def receipt_checker(claim):

    missing_receipts = []

    for expense in claim.get("expenses", []):

        if (
            expense.get("receipt_required", False)
            and not expense.get("receipt_present", False)
        ):
            missing_receipts.append({
                "category": expense.get("category"),
                "amount": expense.get("amount")
            })

    return {
        "missing_receipts": missing_receipts,
        "status": (
            "MISSING"
            if missing_receipts
            else "COMPLETE"
        )
    }
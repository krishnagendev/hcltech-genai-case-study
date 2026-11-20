LIMITS = {
    "meals": 75,
    "lodging": 200,
    "ground_transport": 50
}


def per_diem_limit_checker(claim):

    results = []

    total_allowed = 0
    total_deducted = 0

    for expense in claim.get("expenses", []):

        category = expense.get("category")
        amount = float(expense.get("amount", 0))

        if category in LIMITS:

            units = (
                expense.get("days", 1)
                if category != "lodging"
                else expense.get("nights", 1)
            )

            maximum = LIMITS[category] * units

            allowed = min(amount, maximum)

        else:
            allowed = amount

        deducted = amount - allowed

        total_allowed += allowed
        total_deducted += deducted

        results.append({
            "category": category,
            "claimed": amount,
            "allowed": allowed,
            "deducted": deducted
        })

    return {
        "items": results,
        "calculated_allowed": round(total_allowed, 2),
        "calculated_deducted": round(total_deducted, 2)
    }
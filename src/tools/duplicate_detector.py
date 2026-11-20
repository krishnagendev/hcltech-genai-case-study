def duplicate_detector(claim):

    seen = set()
    duplicates = []

    for expense in claim.get("expenses", []):

        key = (
            expense.get("category"),
            expense.get("amount"),
            expense.get("date")
        )

        if key in seen:
            duplicates.append(expense)
        else:
            seen.add(key)

    return {
        "duplicates": duplicates,
        "duplicate_found": bool(duplicates)
    }
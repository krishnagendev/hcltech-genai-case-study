def approval_threshold_checker(amount):

    if amount <= 1000:
        level = "MANAGER"

    elif amount <= 5000:
        level = "DIRECTOR"

    else:
        level = "SENIOR_DIRECTOR"

    return {
        "amount": amount,
        "approval_level": level,
        "manual_review": amount > 5000
    }
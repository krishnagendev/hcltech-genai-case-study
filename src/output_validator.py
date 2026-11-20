
REQUIRED_FIELDS = {
    "claim_id",
    "decision",
    "approved_amount",
    "deducted_amount",
    "missing_docs",
    "policy_refs",
    "confidence",
    "explanation",
    "tools_used"
}


def validate_output(result):

    missing_fields = REQUIRED_FIELDS - set(result.keys())

    if missing_fields:
        raise ValueError(
            f"Missing output fields: {missing_fields}"
        )

    return True

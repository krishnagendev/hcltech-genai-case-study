from src.tools.policy_lookup import policy_lookup
from src.tools.receipt_checker import receipt_checker
from src.tools.limit_checker import per_diem_limit_checker
from src.tools.timeliness_checker import timeliness_checker
from src.tools.duplicate_detector import duplicate_detector
from src.tools.approval_checker import approval_threshold_checker


def run_agent_tools(claim):

    receipt_result = receipt_checker(claim)

    limit_result = per_diem_limit_checker(claim)

    duplicate_result = duplicate_detector(claim)

    approval_result = approval_threshold_checker(
        limit_result["calculated_allowed"]
    )

    return {
        "receipt": receipt_result,
        "limits": limit_result,
        "duplicates": duplicate_result,
        "approval": approval_result
    }
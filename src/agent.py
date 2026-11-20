from src.policy_engine import run_agent_tools
from src.decision_engine import evaluate_claim


def process_claim(claim):

    print(f"Processing claim: {claim['claim_id']}")

    # Execute agent tools
    tool_results = run_agent_tools(claim)

    # Generate reimbursement decision
    result = evaluate_claim(
        claim,
        tool_results
    )

    return result
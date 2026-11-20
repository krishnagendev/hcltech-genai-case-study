import os
from dotenv import load_dotenv

load_dotenv()

CURRENCY = "USD"

POLICY_VERSION = "Mock Travel Policy — Appendix A"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)

USE_LLM_TOOL_SELECTION = bool(OPENAI_API_KEY)

print("Environment ready.")

print(
    "Optional live LLM tool selection:",
    "enabled (API key found)"
    if USE_LLM_TOOL_SELECTION
    else "disabled (local planner will be used)"
)
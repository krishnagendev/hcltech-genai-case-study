import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

POLICY_FILE = BASE_DIR / "data" / "travel_policy.json"


def load_policies():
    with open(POLICY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def policy_lookup(category):
    policies = load_policies()

    return [
        policy
        for policy in policies
        if policy["category"].lower() == category.lower()
    ]
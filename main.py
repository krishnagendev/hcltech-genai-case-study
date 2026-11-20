import json
from pathlib import Path

from src.agent import process_claim
from src.output_validator import validate_output

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "data" / "sample_claims.json"

OUTPUT_FILE = (
    BASE_DIR / "outputs" / "reimbursement_results.json"
)


def main():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        claims = json.load(file)

    results = []

    for claim in claims:

        result = process_claim(claim)

        # Validate output structure
        validate_output(result)

        results.append(result)

        print(result)

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print("\nProject execution completed.")
    print(f"Results saved at: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
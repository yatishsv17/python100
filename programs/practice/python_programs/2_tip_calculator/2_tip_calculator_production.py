"""
Tip Calculator - Production Version
=====================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner
2. Prompt for total bill amount
   a. Validate: must be a positive number
   b. Warn if unusually high (> $10,000) or low (< $1)
3. Prompt for tip percentage
   a. Validate: must be 10, 12, or 15
4. Prompt for number of people
   a. Validate: must be a positive integer
   b. Warn if unusually high (> 20)
5. Calculate tip amount, total bill, and per-person amount
6. Display detailed breakdown
7. Allow user to calculate again or exit

INPUTS:
- Total bill amount (float): Greater than 0
- Tip percentage (int): 10, 12, or 15
- Number of people (int): Greater than 0

OUTPUTS:
- Detailed breakdown: bill, tip amount, total, per-person amount
- Warning messages for unusual values
- Error messages for invalid inputs

SIDE EFFECTS:
- None

RULES:
- Bill must be > 0
- Tip must be exactly 10, 12, or 15
- People must be > 0
- Equal split among all people

ASSUMPTIONS:
- Currency is in dollars (or equivalent decimal currency)
- All people pay the same amount
- Rounding to 2 decimal places is acceptable

DEPENDENCIES:
- None (standard library only)
"""

import sys
from typing import Optional

VALID_TIP_PERCENTAGES = (10, 12, 15)
MAX_RETRIES = 3


def get_bill_amount() -> Optional[float]:
    """Prompt and validate the bill amount.

    Returns:
        A positive float, or None if retries exhausted.
    """
    for attempt in range(MAX_RETRIES):
        raw = input("What was the total bill? $").strip()
        try:
            bill = float(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a valid number.")
            continue
        if bill <= 0:
            print("  Error: Bill must be greater than $0.")
            continue
        if bill > 10_000:
            print(f"  Warning: ${bill:.2f} seems unusually high.")
        elif bill < 1:
            print(f"  Warning: ${bill:.2f} seems unusually low.")
        return bill
    return None


def get_tip_percentage() -> Optional[int]:
    """Prompt and validate the tip percentage.

    Returns:
        A valid tip percentage, or None if retries exhausted.
    """
    options = ", ".join(str(p) for p in VALID_TIP_PERCENTAGES)
    for attempt in range(MAX_RETRIES):
        raw = input(f"How much tip would you like to give? {options}? ").strip()
        try:
            tip = int(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a valid integer.")
            continue
        if tip not in VALID_TIP_PERCENTAGES:
            print(f"  Error: Tip must be one of {options}.")
            continue
        return tip
    return None


def get_number_of_people() -> Optional[int]:
    """Prompt and validate the number of people.

    Returns:
        A positive integer, or None if retries exhausted.
    """
    for attempt in range(MAX_RETRIES):
        raw = input("How many people to split the bill? ").strip()
        try:
            people = int(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a valid integer.")
            continue
        if people <= 0:
            print("  Error: Number of people must be at least 1.")
            continue
        if people > 20:
            print(f"  Warning: Splitting among {people} people is a large group.")
        return people
    return None


def calculate_split(bill: float, tip_pct: int, people: int) -> dict:
    """Calculate the bill split.

    Args:
        bill: Total bill amount.
        tip_pct: Tip percentage (10, 12, or 15).
        people: Number of people splitting.

    Returns:
        Dictionary with tip_amount, total, and per_person.
    """
    tip_amount = bill * (tip_pct / 100)
    total = bill + tip_amount
    per_person = round(total / people, 2)
    return {
        "tip_amount": round(tip_amount, 2),
        "total": round(total, 2),
        "per_person": per_person,
    }


def display_result(bill: float, tip_pct: int, people: int, result: dict) -> None:
    """Display a detailed breakdown of the calculation.

    Args:
        bill: Original bill amount.
        tip_pct: Tip percentage chosen.
        people: Number of people splitting.
        result: Calculation results dictionary.
    """
    print("\n--- Bill Breakdown ---")
    print(f"  Bill amount:     ${bill:.2f}")
    print(f"  Tip ({tip_pct}%):       ${result['tip_amount']:.2f}")
    print(f"  Total:           ${result['total']:.2f}")
    print(f"  Split {people} way(s):  ${result['per_person']:.2f} each")
    print("----------------------\n")


def run() -> None:
    """Main program loop."""
    print("=" * 35)
    print("   Welcome to the Tip Calculator!")
    print("=" * 35)
    print()

    while True:
        bill = get_bill_amount()
        if bill is None:
            print("Could not get valid bill amount. Exiting.")
            sys.exit(1)

        tip_pct = get_tip_percentage()
        if tip_pct is None:
            print("Could not get valid tip percentage. Exiting.")
            sys.exit(1)

        people = get_number_of_people()
        if people is None:
            print("Could not get valid number of people. Exiting.")
            sys.exit(1)

        result = calculate_split(bill, tip_pct, people)
        display_result(bill, tip_pct, people, result)

        again = input("Calculate another bill? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for using the Tip Calculator!")
            break
        print()


if __name__ == "__main__":
    run()

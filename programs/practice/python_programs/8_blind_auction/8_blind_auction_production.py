"""
Blind Auction - Production Version
=====================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner
2. Bidding loop:
   a. Prompt bidder name (validated: non-empty, alpha + spaces)
   b. Prompt bid amount (validated: positive float)
   c. Store bid (warn if name already exists, overwrite)
   d. Ask if more bidders
   e. Clear screen between bidders
3. After all bids:
   a. Find highest bidder using max()
   b. Display winner with full auction statistics
   c. Show bid range, average, total bidders

INPUTS:
- Bidder name (str): Non-empty, alphabetic + spaces
- Bid amount (float): > 0
- Continue choice (str): 'yes' or 'no'

OUTPUTS:
- Winner announcement (console)
- Auction statistics: bidders count, highest/lowest/average bid (console)
- Error/warning messages (console)

SIDE EFFECTS:
- Clears terminal screen between bidders (os.system)

RULES:
- Highest bid wins
- Same name overwrites previous bid (with warning)
- At least one bidder required

ASSUMPTIONS:
- Terminal supports cls/clear
- Bidders share the same computer

DEPENDENCIES:
- os (standard library)
"""

import os
from typing import Optional

MAX_RETRIES = 3


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_bidder_name() -> Optional[str]:
    """Prompt for a valid bidder name.

    Returns:
        A validated name string, or None if retries exhausted.
    """
    for _ in range(MAX_RETRIES):
        raw = input("What is your name? ").strip()
        if not raw:
            print("  Error: Name cannot be empty.")
            continue
        if not raw.replace(" ", "").isalpha():
            print("  Error: Name must contain only letters and spaces.")
            continue
        return raw.title()
    return None


def get_bid_amount() -> Optional[float]:
    """Prompt for a valid bid amount.

    Returns:
        A positive float, or None if retries exhausted.
    """
    for _ in range(MAX_RETRIES):
        raw = input("What is your bid? $").strip()
        try:
            bid = float(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a valid number.")
            continue
        if bid <= 0:
            print("  Error: Bid must be greater than $0.")
            continue
        return bid
    return None


def find_winner(bids: dict[str, float]) -> tuple[str, float]:
    """Find the highest bidder.

    Args:
        bids: Dictionary mapping bidder names to bid amounts.

    Returns:
        Tuple of (winner_name, winning_bid).
    """
    winner = max(bids, key=bids.get)
    return winner, bids[winner]


def display_results(bids: dict[str, float]) -> None:
    """Display auction results and statistics.

    Args:
        bids: Dictionary of all bids.
    """
    winner, winning_bid = find_winner(bids)
    amounts = list(bids.values())

    print("\n" + "=" * 40)
    print("         AUCTION RESULTS")
    print("=" * 40)
    print(f"\n  Winner: {winner}")
    print(f"  Winning Bid: ${winning_bid:.2f}")
    print(f"\n--- Statistics ---")
    print(f"  Total bidders:  {len(bids)}")
    print(f"  Highest bid:    ${max(amounts):.2f}")
    print(f"  Lowest bid:     ${min(amounts):.2f}")
    print(f"  Average bid:    ${sum(amounts) / len(amounts):.2f}")
    print(f"------------------\n")


def run() -> None:
    """Main program loop."""
    print("=" * 40)
    print("       Blind Auction")
    print("=" * 40)
    print()

    bids: dict[str, float] = {}

    while True:
        name = get_bidder_name()
        if name is None:
            print("Could not get valid name. Skipping bidder.")
            continue

        if name in bids:
            print(f"  Warning: '{name}' already bid ${bids[name]:.2f}. "
                  f"New bid will overwrite.")

        bid = get_bid_amount()
        if bid is None:
            print("Could not get valid bid. Skipping bidder.")
            continue

        bids[name] = bid
        print(f"  Bid recorded for {name}.\n")

        more = input("Are there any other bidders? (yes/no): ").strip().lower()
        if more == "yes":
            clear_screen()
        else:
            break

    if not bids:
        print("No valid bids were placed. Auction cancelled.")
        return

    display_results(bids)


if __name__ == "__main__":
    run()

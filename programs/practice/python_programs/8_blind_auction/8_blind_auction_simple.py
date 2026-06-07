"""
Blind Auction - Simple Version
================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome message
2. Loop: ask each bidder for name and bid amount
3. Ask if there are more bidders
4. Clear screen between bidders
5. After all bids, find the highest bidder
6. Announce the winner

INPUTS:
- Bidder name (str): Name of the person
- Bid amount (float): Dollar amount > 0
- Continue (str): 'yes' or 'no' for more bidders

OUTPUTS:
- Winner name and winning bid amount (console)

SIDE EFFECTS:
- Clears terminal screen between bidders (os.system)

RULES:
- Highest bid wins
- Screen clears between bidders for secrecy
- Same name overwrites previous bid

ASSUMPTIONS:
- Terminal supports screen clearing
- Bidders take turns at same computer

DEPENDENCIES:
- os (standard library)
"""

import os

print("Welcome to the Blind Auction!")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more == "yes":
        os.system("cls" if os.name == "nt" else "clear")
    else:
        continue_bidding = False

winner = max(bids, key=bids.get)
print(f"\nThe winner is {winner} with a bid of ${bids[winner]:.2f}!")

"""
Tip Calculator - Simple Version
================================

WHAT THIS PROGRAM DOES (Flow):
1. Ask user for the total bill amount
2. Ask for the tip percentage (10, 12, or 15)
3. Ask for the number of people splitting the bill
4. Calculate: (bill + tip) / number of people
5. Print the amount each person should pay

INPUTS:
- Total bill amount (float): Must be > 0
- Tip percentage (int): 10, 12, or 15
- Number of people (int): Must be > 0

OUTPUTS:
- Amount each person should pay (formatted to 2 decimal places)

SIDE EFFECTS:
- None

RULES:
- Bill > 0, tip in {10, 12, 15}, people > 0
- Equal split among all people

ASSUMPTIONS:
- User enters valid numbers
- Currency is in dollars

DEPENDENCIES:
- None
"""

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip / 100)
total = bill + tip_amount
per_person = total / people

print(f"Each person should pay: ${per_person:.2f}")

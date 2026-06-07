"""
Password Generator - Simple Version
=====================================

WHAT THIS PROGRAM DOES (Flow):
1. Ask user how many letters they want
2. Ask how many symbols they want
3. Ask how many numbers they want
4. Generate random characters from each category
5. Combine and shuffle all characters
6. Print the generated password

INPUTS:
- Number of letters (int): >= 0
- Number of symbols (int): >= 0
- Number of numbers (int): >= 0

OUTPUTS:
- Generated random password (console)

SIDE EFFECTS:
- None

RULES:
- At least one character type must be > 0
- Password is shuffled for randomness

ASSUMPTIONS:
- Standard ASCII character sets
- User wants a single password

DEPENDENCIES:
- random (standard library)
"""

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
numbers = "0123456789"

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = "".join(password_list)
print(f"Your password is: {password}")

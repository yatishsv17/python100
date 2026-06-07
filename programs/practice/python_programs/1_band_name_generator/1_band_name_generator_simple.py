"""
Band Name Generator - Simple Version
=====================================

WHAT THIS PROGRAM DOES (Flow):
1. Welcome the user to the Band Name Generator
2. Ask for the city they grew up in
3. Ask for their pet's name
4. Combine city + pet name into a band name
5. Print the generated band name

INPUTS:
- City name (string): The city where the user grew up
- Pet name (string): The name of the user's pet

OUTPUTS:
- A generated band name combining city and pet name (console output)

SIDE EFFECTS:
- None. This is a pure console I/O program.

RULES:
- Both inputs must be non-empty
- Band name is simply city + pet name concatenated with a space

ASSUMPTIONS:
- User provides meaningful English text inputs
- No input validation beyond basic non-empty check

DEPENDENCIES:
- None (standard library only)
"""

print("Welcome to the Band Name Generator!")

city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

band_name = city + " " + pet
print(f"Your band name could be: {band_name}")

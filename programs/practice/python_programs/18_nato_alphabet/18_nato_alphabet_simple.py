"""
NATO Phonetic Alphabet - Simple Version
==========================================

WHAT THIS PROGRAM DOES (Flow):
1. Define NATO phonetic alphabet dictionary (A=Alfa, B=Bravo, etc.)
2. Ask user for a word
3. Convert each letter to its NATO phonetic equivalent
4. Print the list of NATO words

INPUTS:
- User word (str): Any string containing letters

OUTPUTS:
- List of NATO phonetic words for each letter (console)

SIDE EFFECTS:
- None

RULES:
- Input converted to uppercase before lookup
- Non-alphabetic characters are ignored
- Case-insensitive

ASSUMPTIONS:
- User wants standard NATO phonetic alphabet
- Simple dictionary lookup is adequate

DEPENDENCIES:
- None
"""

NATO_ALPHABET = {
    "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta",
    "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
    "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
    "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu",
}

word = input("Enter a word: ").upper()

result = [NATO_ALPHABET[letter] for letter in word if letter in NATO_ALPHABET]

print(result)

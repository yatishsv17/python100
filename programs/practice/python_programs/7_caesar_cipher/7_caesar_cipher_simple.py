"""
Caesar Cipher - Simple Version
================================

WHAT THIS PROGRAM DOES (Flow):
1. Ask user for direction: 'encrypt' or 'decrypt'
2. Ask for the text message
3. Ask for the shift number
4. Shift each letter by the given amount (forward for encrypt, backward for decrypt)
5. Print the result

INPUTS:
- Direction (str): 'encrypt' or 'decrypt'
- Text (str): The message to process
- Shift (int): Number of positions to shift

OUTPUTS:
- Encrypted or decrypted text (console)

SIDE EFFECTS:
- None

RULES:
- Encrypt: shift letters forward in alphabet
- Decrypt: shift letters backward in alphabet
- Preserve case and non-alphabetic characters
- Wraps around (Z → A, z → a)

ASSUMPTIONS:
- English alphabet only (A-Z, a-z)
- User enters valid direction and shift

DEPENDENCIES:
- None
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n").lower()
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

shift = shift % 26

def caesar(plain_text, shift_amount, direction):
    result = ""
    if direction == "decrypt":
        shift_amount *= -1

    for char in plain_text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            index = alphabet.index(char.lower())
            new_index = (index + shift_amount) % 26
            new_char = alphabet[new_index]
            result += new_char.upper() if is_upper else new_char
        else:
            result += char
    return result

result = caesar(text, shift, direction)
print(f"The {direction}ed text is: {result}")

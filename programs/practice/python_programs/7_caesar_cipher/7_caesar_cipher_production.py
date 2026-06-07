"""
Caesar Cipher - Production Version
=====================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner
2. Prompt for direction (encrypt/decrypt) with validation
3. Prompt for text message (non-empty validation)
4. Prompt for shift number (non-negative integer validation)
5. Normalize shift to 0-25 range using modulo
6. Process each character:
   a. Alphabetic → shift by offset, preserve case
   b. Non-alphabetic → preserve as-is
7. Display result with operation summary
8. Offer to process another message or exit

INPUTS:
- Direction (str): 'encrypt' or 'decrypt' (case-insensitive)
- Text (str): Non-empty message string
- Shift (int): Non-negative integer

OUTPUTS:
- Encrypted/decrypted text (console)
- Operation summary (console)
- Error messages for invalid inputs (console)

SIDE EFFECTS:
- None

RULES:
- Encryption: shift letters forward
- Decryption: shift letters backward
- Preserve case (uppercase/lowercase)
- Preserve non-alphabetic characters (spaces, punctuation, digits)
- Wraps around alphabet using modulo 26

ASSUMPTIONS:
- English alphabet only (A-Z, a-z)
- Non-alphabetic characters pass through unchanged

DEPENDENCIES:
- None (standard library only)
"""

from typing import Optional

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = 26
MAX_RETRIES = 3


def get_direction() -> Optional[str]:
    """Prompt for encrypt or decrypt direction.

    Returns:
        'encrypt' or 'decrypt', or None if retries exhausted.
    """
    for _ in range(MAX_RETRIES):
        raw = input("Type 'encrypt' or 'decrypt': ").strip().lower()
        if raw in ("encrypt", "decrypt"):
            return raw
        print(f"  Error: '{raw}' is not valid. Choose 'encrypt' or 'decrypt'.")
    return None


def get_text() -> Optional[str]:
    """Prompt for the message text.

    Returns:
        Non-empty text string, or None if retries exhausted.
    """
    for _ in range(MAX_RETRIES):
        raw = input("Type your message: ").strip()
        if raw:
            return raw
        print("  Error: Message cannot be empty.")
    return None


def get_shift() -> Optional[int]:
    """Prompt for the shift number.

    Returns:
        A non-negative integer, or None if retries exhausted.
    """
    for _ in range(MAX_RETRIES):
        raw = input("Type the shift number: ").strip()
        try:
            shift = int(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a valid integer.")
            continue
        if shift < 0:
            print("  Error: Shift must be >= 0.")
            continue
        return shift
    return None


def caesar_cipher(text: str, shift: int, direction: str) -> str:
    """Apply Caesar cipher to the given text.

    Args:
        text: The message to encrypt or decrypt.
        shift: Number of positions to shift (0-25 after normalization).
        direction: 'encrypt' (shift forward) or 'decrypt' (shift backward).

    Returns:
        The processed text.
    """
    shift = shift % ALPHABET_SIZE
    if direction == "decrypt":
        shift = -shift

    result = []
    for char in text:
        if char.lower() in ALPHABET:
            is_upper = char.isupper()
            index = ALPHABET.index(char.lower())
            new_index = (index + shift) % ALPHABET_SIZE
            new_char = ALPHABET[new_index]
            result.append(new_char.upper() if is_upper else new_char)
        else:
            result.append(char)

    return "".join(result)


def display_result(direction: str, original: str, result: str, shift: int) -> None:
    """Display the cipher operation result.

    Args:
        direction: 'encrypt' or 'decrypt'.
        original: The original text.
        result: The processed text.
        shift: The shift amount used.
    """
    print(f"\n--- Caesar Cipher Result ---")
    print(f"  Operation:  {direction.title()}")
    print(f"  Shift:      {shift}")
    print(f"  Original:   {original}")
    print(f"  Result:     {result}")
    alpha_count = sum(1 for c in original if c.isalpha())
    print(f"  Characters shifted: {alpha_count}")
    print(f"----------------------------\n")


def run() -> None:
    """Main program loop."""
    print("=" * 35)
    print("      Caesar Cipher")
    print("=" * 35)
    print()

    while True:
        direction = get_direction()
        if direction is None:
            print("Exiting.")
            return

        text = get_text()
        if text is None:
            print("Exiting.")
            return

        shift = get_shift()
        if shift is None:
            print("Exiting.")
            return

        result = caesar_cipher(text, shift, direction)
        display_result(direction, text, result, shift % ALPHABET_SIZE)

        again = input("Process another message? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    run()

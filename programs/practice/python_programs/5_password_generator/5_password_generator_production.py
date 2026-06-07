"""
Password Generator - Production Version
=========================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner
2. Prompt for number of letters (validate: non-negative int)
3. Prompt for number of symbols (validate: non-negative int)
4. Prompt for number of numbers (validate: non-negative int)
5. Ensure total length > 0
6. Generate random characters using secrets module (cryptographically secure)
7. Shuffle and combine into final password
8. Display password with composition breakdown
9. Provide security recommendations based on password strength
10. Allow generating another password or exit

INPUTS:
- Number of letters (int): >= 0
- Number of symbols (int): >= 0
- Number of numbers (int): >= 0

OUTPUTS:
- Generated password (console)
- Password composition breakdown (console)
- Security strength assessment (console)

SIDE EFFECTS:
- None

RULES:
- All counts must be non-negative integers
- Total length must be > 0
- Password is cryptographically randomly generated

ASSUMPTIONS:
- Standard character sets are acceptable
- User wants one password per request

DEPENDENCIES:
- secrets (standard library, Python 3.6+)
- string (standard library)
"""

import secrets
import string
from typing import Optional

LETTERS = string.ascii_letters
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"
DIGITS = string.digits

MAX_RETRIES = 3


def get_non_negative_int(prompt: str, field_name: str) -> Optional[int]:
    """Prompt for a non-negative integer.

    Args:
        prompt: The prompt to display.
        field_name: Name of the field for error messages.

    Returns:
        A non-negative integer, or None if retries exhausted.
    """
    for _ in range(MAX_RETRIES):
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a valid integer.")
            continue
        if value < 0:
            print(f"  Error: {field_name} cannot be negative.")
            continue
        return value
    return None


def generate_password(nr_letters: int, nr_symbols: int, nr_numbers: int) -> str:
    """Generate a cryptographically secure random password.

    Args:
        nr_letters: Number of letter characters.
        nr_symbols: Number of symbol characters.
        nr_numbers: Number of digit characters.

    Returns:
        A shuffled password string.
    """
    chars = []
    for _ in range(nr_letters):
        chars.append(secrets.choice(LETTERS))
    for _ in range(nr_symbols):
        chars.append(secrets.choice(SYMBOLS))
    for _ in range(nr_numbers):
        chars.append(secrets.choice(DIGITS))

    # Shuffle using secrets-compatible method
    password_list = list(chars)
    # Fisher-Yates shuffle using secrets
    for i in range(len(password_list) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_list[i], password_list[j] = password_list[j], password_list[i]

    return "".join(password_list)


def assess_strength(length: int, has_letters: bool, has_symbols: bool,
                    has_numbers: bool) -> str:
    """Assess password strength.

    Args:
        length: Total password length.
        has_letters: Whether password contains letters.
        has_symbols: Whether password contains symbols.
        has_numbers: Whether password contains numbers.

    Returns:
        Strength assessment string.
    """
    variety = sum([has_letters, has_symbols, has_numbers])
    if length >= 16 and variety == 3:
        return "Strong"
    if length >= 12 and variety >= 2:
        return "Good"
    if length >= 8:
        return "Fair"
    return "Weak"


def display_result(password: str, nr_letters: int, nr_symbols: int,
                   nr_numbers: int) -> None:
    """Display generated password with details.

    Args:
        password: The generated password.
        nr_letters: Count of letters.
        nr_symbols: Count of symbols.
        nr_numbers: Count of digits.
    """
    total = len(password)
    strength = assess_strength(
        total,
        nr_letters > 0,
        nr_symbols > 0,
        nr_numbers > 0,
    )

    print(f"\n  Password:    {password}")
    print(f"  Length:      {total}")
    print(f"  Composition: {nr_letters} letters, {nr_symbols} symbols, "
          f"{nr_numbers} numbers")
    print(f"  Strength:   {strength}")

    if strength == "Weak":
        print("  Recommendation: Use at least 12 characters with all 3 types.")
    elif strength == "Fair":
        print("  Recommendation: Add more character variety for better security.")
    print()


def run() -> None:
    """Main program loop."""
    print("=" * 40)
    print("   Secure Password Generator")
    print("=" * 40)
    print()

    while True:
        nr_letters = get_non_negative_int("How many letters? ", "Letters")
        if nr_letters is None:
            print("Exiting.")
            return

        nr_symbols = get_non_negative_int("How many symbols? ", "Symbols")
        if nr_symbols is None:
            print("Exiting.")
            return

        nr_numbers = get_non_negative_int("How many numbers? ", "Numbers")
        if nr_numbers is None:
            print("Exiting.")
            return

        total = nr_letters + nr_symbols + nr_numbers
        if total == 0:
            print("  Error: Password must have at least 1 character.\n")
            continue

        password = generate_password(nr_letters, nr_symbols, nr_numbers)
        display_result(password, nr_letters, nr_symbols, nr_numbers)

        again = input("Generate another? (yes/no): ").strip().lower()
        if again != "yes":
            print("Stay secure!")
            break
        print()


if __name__ == "__main__":
    run()

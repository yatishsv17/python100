"""
Band Name Generator - Production Version
==========================================

WHAT THIS PROGRAM DOES (Flow):
1. Display welcome banner
2. Prompt user for city name
   a. Validate: non-empty, >= 2 chars, alphabetic (spaces allowed)
   b. Retry up to MAX_RETRIES times on invalid input
3. Prompt user for pet name (same validation as city)
4. Generate band names in multiple styles:
   - Classic:  "The {City} {Pet}"
   - Reversed: "The {Pet} {City}"
   - With Of:  "{Pet} of {City}"
   - Modern:   "{City} & The {Pet}s"
5. Display all generated band names with style labels
6. Allow user to run again or exit

INPUTS:
- City name (str): Alphabetic characters and spaces, >= 2 chars
- Pet name (str):  Alphabetic characters and spaces, >= 2 chars
- Play again (str): 'yes' or 'no'

OUTPUTS:
- Multiple band name variations with style labels (console output)
- Error messages for invalid inputs (console output)

SIDE EFFECTS:
- None. Pure console I/O program.

RULES:
- Both inputs must be non-empty, at least 2 characters, alphabetic only
- Input validation with retry logic (max 3 retries per input)
- Multiple band name styles generated per run
- User can run multiple times

ASSUMPTIONS:
- User provides English alphabetic inputs
- City and pet names are real and meaningful
- Band names should be properly title-cased

DEPENDENCIES:
- None (standard library only)
"""

import sys
from typing import Optional

MAX_RETRIES = 3

BAND_NAME_STYLES = {
    "Classic": "The {city} {pet}",
    "Reversed": "The {pet} {city}",
    "With Of": "{pet} of {city}",
    "Modern": "{city} & The {pet}s",
}


def validate_input(text: str, field_name: str) -> Optional[str]:
    """Validate user input for city or pet name.

    Args:
        text: The raw input string from the user.
        field_name: Name of the field (for error messages).

    Returns:
        The cleaned, title-cased string if valid; None otherwise.
    """
    cleaned = text.strip()
    if not cleaned:
        print(f"  Error: {field_name} cannot be empty.")
        return None
    if len(cleaned) < 2:
        print(f"  Error: {field_name} must be at least 2 characters.")
        return None
    if not cleaned.replace(" ", "").isalpha():
        print(f"  Error: {field_name} must contain only alphabetic characters.")
        return None
    return cleaned.title()


def get_valid_input(prompt: str, field_name: str) -> Optional[str]:
    """Prompt the user repeatedly until valid input is provided or retries exhausted.

    Args:
        prompt: The prompt message to display.
        field_name: Name of the field being collected.

    Returns:
        A validated, title-cased string, or None if retries exhausted.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        raw = input(prompt)
        result = validate_input(raw, field_name)
        if result is not None:
            return result
        remaining = MAX_RETRIES - attempt
        if remaining > 0:
            print(f"  ({remaining} attempt(s) remaining)\n")
    print(f"  Max retries reached for {field_name}.")
    return None


def generate_band_names(city: str, pet: str) -> list[tuple[str, str]]:
    """Generate band names in multiple styles.

    Args:
        city: Validated city name.
        pet: Validated pet name.

    Returns:
        List of (style_name, band_name) tuples.
    """
    results = []
    for style, template in BAND_NAME_STYLES.items():
        name = template.format(city=city, pet=pet)
        results.append((style, name))
    return results


def display_banner() -> None:
    """Display the welcome banner."""
    print("=" * 45)
    print("   Welcome to the Band Name Generator!")
    print("=" * 45)
    print()


def run() -> None:
    """Main program loop."""
    display_banner()

    while True:
        city = get_valid_input(
            "What's the name of the city you grew up in? ", "City name"
        )
        if city is None:
            print("Could not get valid city name. Exiting.\n")
            sys.exit(1)

        pet = get_valid_input("What's your pet's name? ", "Pet name")
        if pet is None:
            print("Could not get valid pet name. Exiting.\n")
            sys.exit(1)

        band_names = generate_band_names(city, pet)

        print("\nYour band name could be:\n")
        for style, name in band_names:
            print(f"  [{style:>10}]  {name}")
        print()

        again = input("Generate another? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for using the Band Name Generator! Rock on!")
            break
        print()


if __name__ == "__main__":
    run()

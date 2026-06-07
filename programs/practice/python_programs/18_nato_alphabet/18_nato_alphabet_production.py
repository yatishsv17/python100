"""
NATO Phonetic Alphabet - Production Version
=============================================

WHAT THIS PROGRAM DOES (Flow):
1. Define NATO phonetic alphabet dictionary
2. Prompt user for a word (validated: non-empty, contains letters)
3. Convert to uppercase
4. For each character:
   a. If alphabetic → look up NATO word
   b. If non-alphabetic → skip (note it)
5. Display result in formatted output
6. Show conversion summary (letters converted, non-alpha skipped)
7. Allow converting another word or exit

INPUTS:
- User word (str): Non-empty string containing at least one letter

OUTPUTS:
- NATO phonetic words for each letter (console)
- Conversion summary (console)
- Error messages for invalid input (console)

SIDE EFFECTS:
- None

RULES:
- Input converted to uppercase before lookup
- Non-alphabetic characters logged and skipped
- Case-insensitive

ASSUMPTIONS:
- Standard NATO phonetic alphabet
- Simple dictionary lookup

DEPENDENCIES:
- None (standard library only)
"""

from typing import Optional

NATO_ALPHABET = {
    "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta",
    "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
    "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
    "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu",
}


def get_word() -> Optional[str]:
    """Prompt for a non-empty word containing at least one letter.

    Returns:
        The input word, or None if retries exhausted.
    """
    for _ in range(3):
        raw = input("Enter a word: ").strip()
        if not raw:
            print("  Error: Input cannot be empty.")
            continue
        if not any(c.isalpha() for c in raw):
            print("  Error: Input must contain at least one letter.")
            continue
        return raw
    return None


def convert_to_nato(word: str) -> tuple[list[str], int]:
    """Convert a word to NATO phonetic alphabet equivalents.

    Args:
        word: The input word.

    Returns:
        Tuple of (list of NATO words, count of skipped non-alpha chars).
    """
    result = []
    skipped = 0
    for char in word.upper():
        if char in NATO_ALPHABET:
            result.append(NATO_ALPHABET[char])
        elif not char.isspace():
            skipped += 1
    return result, skipped


def display_result(word: str, nato_words: list[str], skipped: int) -> None:
    """Display the conversion result.

    Args:
        word: Original input word.
        nato_words: List of NATO phonetic words.
        skipped: Number of non-alpha characters skipped.
    """
    print(f"\n--- NATO Conversion ---")
    print(f"  Input: {word}")
    print(f"  NATO:  {' · '.join(nato_words)}")
    print(f"  Letters converted: {len(nato_words)}")
    if skipped > 0:
        print(f"  Non-alpha skipped: {skipped}")
    print(f"-----------------------\n")


def run() -> None:
    """Main program loop."""
    print("=" * 35)
    print("   NATO Phonetic Alphabet")
    print("=" * 35)
    print()

    while True:
        word = get_word()
        if word is None:
            print("Exiting.")
            return

        nato_words, skipped = convert_to_nato(word)
        display_result(word, nato_words, skipped)

        again = input("Convert another word? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    run()

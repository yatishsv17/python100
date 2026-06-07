"""
Web Scraping Movies - Production Version
==========================================

WHAT THIS PROGRAM DOES (Flow):
1. Define target URL and configuration
2. Send HTTP GET request with retry logic and timeout
3. Validate response status
4. Parse HTML with BeautifulSoup
5. Extract movie titles using CSS selectors
6. Clean and validate extracted titles
7. Reverse list (site lists 100→1, we want 1→100)
8. Write numbered titles to movies.txt
9. Write detailed log to scraping_log.txt
10. Display summary statistics

INPUTS:
- Target URL: Empire Online archived page (hardcoded)
- No user input required

OUTPUTS:
- movies.txt: numbered movie titles (file)
- scraping_log.txt: operation log with timestamps (file)
- Console: progress messages and statistics

SIDE EFFECTS:
- Makes HTTP GET request to external website
- Writes movies.txt and scraping_log.txt to disk

RULES:
- Format: "1. Movie Title" per line
- Retry up to 3 times on connection failure
- Timeout: 10 seconds per request

ASSUMPTIONS:
- Internet connection available
- Target site accessible
- BeautifulSoup and requests installed

DEPENDENCIES:
- requests (pip install requests)
- beautifulsoup4 (pip install beautifulsoup4)
"""

import requests
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
import time

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
MAX_RETRIES = 3
TIMEOUT = 10
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python Scraper"
"https://appbrewery.github.io/instant_pot/"
SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_PATH = SCRIPT_DIR / "movies.txt"
LOG_PATH = SCRIPT_DIR / "scraping_log.txt"


def log_message(message: str, log_lines: list[str]) -> None:
    """Print and store a log message with timestamp.

    Args:
        message: The message to log.
        log_lines: List to append the log entry to.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(f"  {message}")
    log_lines.append(entry)


def fetch_page(url: str, log_lines: list[str]) -> str | None:
    """Fetch the webpage with retry logic.

    Args:
        url: Target URL.
        log_lines: Log message list.

    Returns:
        HTML content string, or None on failure.
    """
    headers = {"User-Agent": USER_AGENT}
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            log_message(f"Attempt {attempt}/{MAX_RETRIES}: Fetching URL...", log_lines)
            response = requests.get(url, headers=headers, timeout=TIMEOUT)
            response.raise_for_status()
            log_message(f"Success: HTTP {response.status_code}, "
                        f"{len(response.text)} chars", log_lines)
            return response.text
        except requests.RequestException as e:
            log_message(f"Error: {e}", log_lines)
            if attempt < MAX_RETRIES:
                wait = attempt * 2
                log_message(f"Retrying in {wait}s...", log_lines)
                time.sleep(wait)
    log_message("All retries exhausted.", log_lines)
    return None


def extract_movies(html: str, log_lines: list[str]) -> list[str]:
    """Parse HTML and extract movie titles.

    Args:
        html: Raw HTML content.
        log_lines: Log message list.

    Returns:
        List of movie titles (ordered 1 to N).
    """
    soup = BeautifulSoup(html, "html.parser")
    movie_tags = soup.find_all(name="h3", class_="title")

    log_message(f"Found {len(movie_tags)} title elements.", log_lines)

    movies = []
    for tag in movie_tags:
        title = tag.getText().strip()
        if title:
            # Remove leading number if present (e.g., "100) The Godfather")
            cleaned = title
            if ")" in cleaned[:5]:
                cleaned = cleaned.split(")", 1)[1].strip()
            movies.append(cleaned)

    movies.reverse()
    log_message(f"Extracted {len(movies)} valid movie titles.", log_lines)
    return movies


def save_movies(movies: list[str], log_lines: list[str]) -> None:
    """Save movies to text file.

    Args:
        movies: Ordered list of movie titles.
        log_lines: Log message list.
    """
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for i, movie in enumerate(movies, 1):
            f.write(f"{i}. {movie}\n")
    log_message(f"Saved {len(movies)} movies to {OUTPUT_PATH.name}", log_lines)


def save_log(log_lines: list[str]) -> None:
    """Save log entries to file.

    Args:
        log_lines: List of log entries.
    """
    LOG_PATH.write_text("\n".join(log_lines), encoding="utf-8")


def run() -> None:
    """Main program entry."""
    print("=" * 45)
    print("   Web Scraping: Top 100 Movies")
    print("=" * 45)
    print()

    log_lines: list[str] = []
    log_message("Starting movie scraper...", log_lines)

    html = fetch_page(URL, log_lines)
    if html is None:
        log_message("Failed to fetch page. Exiting.", log_lines)
        save_log(log_lines)
        return

    movies = extract_movies(html, log_lines)
    if not movies:
        log_message("No movies found. Exiting.", log_lines)
        save_log(log_lines)
        return

    save_movies(movies, log_lines)

    print(f"\n--- Summary ---")
    print(f"  Movies scraped: {len(movies)}")
    print(f"  Output file:    {OUTPUT_PATH.name}")
    print(f"  Log file:       {LOG_PATH.name}")
    print(f"---------------\n")

    log_message("Scraping complete.", log_lines)
    save_log(log_lines)


if __name__ == "__main__":
    run()

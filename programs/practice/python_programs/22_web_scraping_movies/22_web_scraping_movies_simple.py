"""
Web Scraping Movies - Simple Version
=======================================

WHAT THIS PROGRAM DOES (Flow):
1. Send HTTP GET request to target URL (Empire Top 100 movies)
2. Parse HTML with BeautifulSoup
3. Find all movie title elements
4. Extract and clean movie titles
5. Write titles to movies.txt with serial numbers

INPUTS:
- Target URL: Empire Online archived page (hardcoded)
- No user input required

OUTPUTS:
- movies.txt: text file with numbered movie titles (file)
- Console output: progress messages

SIDE EFFECTS:
- Makes HTTP request to external website
- Writes movies.txt to disk

RULES:
- Format: "1. Movie Title" per line
- Serial numbers starting from 1

ASSUMPTIONS:
- Internet connection available
- Target website accessible and structure unchanged
- BeautifulSoup and requests installed

DEPENDENCIES:
- requests (pip install requests)
- beautifulsoup4 (pip install beautifulsoup4)
- os (standard library)
"""

import requests
from bs4 import BeautifulSoup
import os

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "movies.txt")

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
movie_tags = soup.find_all(name="h3", class_="title")

movies = [tag.getText().strip() for tag in movie_tags]
movies.reverse()

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    for i, movie in enumerate(movies, 1):
        line = f"{i}. {movie}"
        f.write(line + "\n")
        print(line)

print(f"\nSaved {len(movies)} movies to movies.txt")

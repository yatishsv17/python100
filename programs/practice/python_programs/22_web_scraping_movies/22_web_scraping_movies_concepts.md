# Web Scraping Movies - Python Concepts

## Core Python Concepts Used

### 1. `requests` Library — HTTP Requests
**Concept:** Fetching web pages programmatically.

```python
import requests
response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()   # Raises HTTPError for 4xx/5xx
html = response.text           # HTML content as string
status = response.status_code  # 200, 404, 500, etc.
```

| Method | Description |
|--------|-------------|
| `requests.get(url)` | HTTP GET request |
| `requests.post(url, data=...)` | HTTP POST request |
| `response.text` | Response body as string (decoded) |
| `response.content` | Response body as bytes (raw) |
| `response.json()` | Parse JSON response into dict/list |
| `response.status_code` | HTTP status code (int) |
| `response.raise_for_status()` | Raise `HTTPError` on 4xx/5xx |
| `response.headers` | Response headers (dict-like) |

**HTTP status codes:**

| Code | Meaning |
|------|---------|
| `200` | OK — request succeeded |
| `301` | Moved permanently (redirect) |
| `403` | Forbidden — access denied |
| `404` | Not found |
| `429` | Too many requests (rate limited) |
| `500` | Internal server error |

**`requests.get()` parameters:**
```python
requests.get(
    url,
    headers={"User-Agent": "..."},  # Custom headers
    params={"q": "python"},          # URL query parameters (?q=python)
    timeout=10,                      # Seconds before giving up
    allow_redirects=True,            # Follow redirects (default)
)
```

### 2. BeautifulSoup — HTML Parsing
**Concept:** Navigating and searching HTML/XML documents.

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find elements
soup.find("h3")                      # First <h3>
soup.find_all("h3", class_="title")  # All <h3 class="title">
tag.getText()                        # Text content of element
tag.get("href")                      # Attribute value
```

| Parser | Speed | Dependencies |
|--------|-------|-------------|
| `"html.parser"` | Moderate | Built-in (standard library) |
| `"lxml"` | Fast | `pip install lxml` |
| `"html5lib"` | Lenient (handles broken HTML) | `pip install html5lib` |

**BeautifulSoup search methods:**
```python
# find() — first match (or None)
tag = soup.find("div", class_="movie")
tag = soup.find("a", {"data-type": "title"})  # Custom attributes

# find_all() — all matches (list, possibly empty)
tags = soup.find_all("h3")
tags = soup.find_all(["h2", "h3"])   # Multiple tag types
tags = soup.find_all(class_="title") # By class only

# select() — CSS selectors (more powerful)
soup.select("div.movie h3")          # Descendant selector
soup.select("a[href^='http']")       # Attribute starts with
soup.select("#main > .title")        # Direct child
```

**Extracting data from tags:**
```python
tag.getText()           # "Movie Title"  (all text, including children)
tag.get_text(strip=True) # "Movie Title" (stripped whitespace)
tag.string              # Direct text content (None if has children)
tag["href"]             # Attribute value (raises KeyError if missing)
tag.get("href")         # Attribute value (returns None if missing)
tag.get("href", "#")    # With default value
```

### 3. Retry Pattern with Exponential Backoff
**Concept:** Retrying failed operations with increasing delays.

```python
for attempt in range(1, MAX_RETRIES + 1):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        if attempt < MAX_RETRIES:
            time.sleep(attempt * 2)  # Exponential backoff: 2s, 4s, 6s
```

**Why exponential backoff?**
- Constant retry → overwhelms server when it's struggling
- Exponential delay → gives server time to recover
- Common pattern: `delay = base * (2 ** attempt)` or `delay = attempt * 2`

**Production retry with `tenacity` library:**
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def fetch_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text
```

### 4. List `.reverse()` vs `reversed()`
**Concept:** Reversing list order — in-place vs new copy.

```python
movies.reverse()         # In-place, returns None
new_list = list(reversed(movies))  # Returns new iterator → list
movies[::-1]             # Slice creates reversed copy
```

**In-place vs copy pattern (common in Python):**

| In-Place (mutates) | Returns Copy |
|--------------------|-------------|
| `list.sort()` → `None` | `sorted(list)` → new list |
| `list.reverse()` → `None` | `reversed(list)` → iterator |
| `list.append(x)` → `None` | `list + [x]` → new list |

**Common bug:**
```python
# BUG: .reverse() returns None, not the list!
reversed_movies = movies.reverse()  # reversed_movies is None!

# FIX:
movies.reverse()          # Mutate in place, then use movies
# OR
reversed_movies = movies[::-1]  # Create a reversed copy
```

### 5. Exception Hierarchy
**Concept:** Using `requests.RequestException` to catch all request errors.

```python
requests.RequestException
  ├── requests.ConnectionError    # Network problem
  ├── requests.Timeout            # Request took too long
  ├── requests.HTTPError          # Raised by raise_for_status()
  └── requests.TooManyRedirects   # Too many redirects
```

**Exception handling best practices:**
```python
# Catch specific exceptions first, general ones last:
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.Timeout:
    print("Request timed out")       # Specific
except requests.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")  # Specific
except requests.RequestException as e:
    print(f"Request failed: {e}")    # General fallback
```

### 6. User-Agent Header and Web Scraping Ethics
**Concept:** Identifying the client to the web server.

```python
headers = {"User-Agent": "Mozilla/5.0 ... Python Scraper"}
response = requests.get(url, headers=headers)
```

- Some sites block requests without a proper User-Agent
- Always be ethical: respect `robots.txt`, don't overload servers

**Web scraping best practices:**
- Check `robots.txt` before scraping (`https://site.com/robots.txt`)
- Add delays between requests (`time.sleep()`)
- Use a descriptive User-Agent identifying your bot
- Cache responses to avoid redundant requests
- Respect `rate-limit` headers (e.g., `429 Too Many Requests`)

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Error handling** | `raise_for_status()` only | Retry logic with exponential backoff |
| **Timeout** | None (hangs forever) | 10 seconds |
| **User-Agent** | Default Python requests | Custom header identifying scraper |
| **Logging** | Print only | Timestamped log file |
| **Title cleaning** | Basic strip | Remove leading numbers |
| **Output** | Console + file | Console + file + log file |
| **Selectors** | Single hardcoded | Could add fallback selectors |

### Why Production is Better
- **Resilience:** Retry logic handles temporary network failures
- **Timeout:** Prevents hanging on slow connections
- **Logging:** Detailed log file for debugging scraping issues
- **Ethical:** User-Agent identifies the scraper honestly
- **Data quality:** Cleans title formatting (removes numbering)
- **Debuggable:** Timestamped logs track what was scraped and when

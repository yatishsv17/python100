# Price Tracker - Python Concepts

## Core Python Concepts Used

### 1. Environment Variables for Secrets
**Concept:** Never hardcode credentials — use environment variables.

```python
import os
EMAIL = os.environ.get("EMAIL_ADDRESS", "")
PASSWORD = os.environ.get("EMAIL_PASSWORD", "")
```

Setting environment variables:
```bash
# Windows PowerShell
$env:EMAIL_ADDRESS = "user@gmail.com"
$env:EMAIL_PASSWORD = "app-password"

# Linux/Mac
export EMAIL_ADDRESS="user@gmail.com"
export EMAIL_PASSWORD="app-password"
```

- `.get(key, default)` returns default if key doesn't exist
- `os.environ[key]` raises `KeyError` if missing

**`os.environ` methods:**

| Method | Missing Key | Use Case |
|--------|-------------|----------|
| `os.environ["KEY"]` | `KeyError` | Required vars (fail fast) |
| `os.environ.get("KEY")` | Returns `None` | Optional vars |
| `os.environ.get("KEY", "default")` | Returns `"default"` | Optional with fallback |

**Alternative: `.env` files with `python-dotenv`:**
```python
# .env file (never commit to git!)
EMAIL_ADDRESS=user@gmail.com
EMAIL_PASSWORD=app-password

# Python
from dotenv import load_dotenv
load_dotenv()  # Reads .env file into os.environ
email = os.environ.get("EMAIL_ADDRESS")
```

**Security best practices:**
- Never hardcode secrets in source code
- Add `.env` to `.gitignore`
- Use different credentials for dev/prod
- Gmail: use "App Passwords", not your real password

### 2. `smtplib` — Sending Emails
**Concept:** Sending emails via SMTP protocol.

```python
import smtplib
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()                        # Enable TLS encryption
    smtp.login(email, password)            # Authenticate
    smtp.sendmail(from_addr, to_addr, msg) # Send
```

- `starttls()` upgrades the connection to encrypted
- Gmail requires "App Passwords" (not regular password)
- `with` statement auto-closes the connection

**SMTP ports:**

| Port | Protocol | Description |
|------|----------|-------------|
| `25` | SMTP | Unencrypted (often blocked) |
| `465` | SMTPS | SSL from start (`SMTP_SSL`) |
| `587` | SMTP + STARTTLS | Starts plain, upgrades to TLS |

**`SMTP` vs `SMTP_SSL`:**
```python
# Port 587 — start plain, upgrade to TLS
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()    # Upgrade connection
    smtp.login(...)

# Port 465 — encrypted from the start
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(...)    # Already encrypted, no starttls needed
```

### 3. `email.mime` — Composing Emails
**Concept:** Building properly formatted email messages.

```python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = "Subject Line"
msg.attach(MIMEText("Body text", "plain"))
smtp.send_message(msg)
```

**`sendmail()` vs `send_message()`:**
```python
# sendmail() — raw string, must manually format headers
smtp.sendmail(from_addr, to_addr, "Subject: Hi\n\nBody text")

# send_message() — uses MIME object, proper headers automatically
smtp.send_message(msg)  # Reads From/To from msg headers
```

**HTML emails:**
```python
msg.attach(MIMEText("<h1>Price Alert!</h1><p>Price dropped to $99</p>", "html"))
```

### 4. `@dataclass` Decorator
**Concept:** Auto-generating `__init__`, `__repr__`, etc. for data classes.

```python
from dataclasses import dataclass

@dataclass
class Config:
    smtp_server: str
    smtp_port: int
    email_address: str
    target_price: float

# Auto-generates:
# def __init__(self, smtp_server, smtp_port, email_address, target_price): ...
# def __repr__(self): ...
# def __eq__(self, other): ...
```

**`@dataclass` options:**
```python
@dataclass(frozen=True)     # Immutable (raises on attribute assignment)
@dataclass(order=True)      # Generates <, <=, >, >= based on fields
@dataclass(slots=True)      # Uses __slots__ (Python 3.10+, faster, less memory)
```

**`@dataclass` vs manual class vs `namedtuple`:**

| Feature | Manual Class | `@dataclass` | `namedtuple` |
|---------|-------------|-------------|--------------|
| `__init__` auto | No | Yes | Yes |
| `__repr__` auto | No | Yes | Yes |
| Mutable | Yes | Yes (default) | No |
| Default values | Manual | `field(default=...)` | Yes |
| Type hints | Optional | Required | Optional |
| Methods | Yes | Yes | Limited |

**Fields with defaults and factories:**
```python
from dataclasses import dataclass, field

@dataclass
class Config:
    name: str
    port: int = 587                              # Simple default
    tags: list[str] = field(default_factory=list) # Mutable default — must use factory!
    # tags: list[str] = []  ← BUG! All instances would share the SAME list
```

### 5. `**kwargs` — Dictionary Unpacking as Arguments
**Concept:** Trying multiple CSS selectors as fallbacks.

```python
selectors = [
    {"id": "priceblock_ourprice"},
    {"class_": "a-price-whole"},
    {"class_": "price"},
]
for selector in selectors:
    tag = soup.find(**selector)   # ** unpacks dict as keyword args
    if tag:
        break
```

**`**` unpacking explained:**
```python
params = {"class_": "price", "id": "main"}
soup.find(**params)
# Equivalent to:
soup.find(class_="price", id="main")

# Single * unpacks iterables:
args = [1, 2, 3]
print(*args)  # print(1, 2, 3)
```

### 6. String Cleaning for Price Parsing
**Concept:** Extracting numeric value from a price string.

```python
price_text = "$1,299.99"
cleaned = ""
for ch in price_text:
    if ch.isdigit() or ch == ".":
        cleaned += ch
# cleaned = "1299.99"
price = float(cleaned)
```

**Alternative approaches:**
```python
# Using regex (more robust)
import re
price = float(re.sub(r"[^\d.]", "", "$1,299.99"))  # 1299.99

# Using str.translate (fastest)
remove = str.maketrans("", "", "$,€£ ")
price = float("$1,299.99".translate(remove))  # 1299.99

# Using list comprehension + join
cleaned = "".join(ch for ch in price_text if ch.isdigit() or ch == ".")
```

### 7. Log Accumulation Pattern
**Concept:** Collecting log messages in a list for batch writing.

```python
log_lines: list[str] = []
def log(message, log_lines):
    log_lines.append(f"[{timestamp}] {message}")
# ... operations ...
save_log(log_lines)  # Write all at once
```

**Why accumulate then write?**
- Fewer file I/O operations (one write vs many)
- Atomic: if script crashes partway, either all logs are written or none
- Can review/filter logs before writing

**Alternative: Python `logging` module (standard library):**
```python
import logging
logging.basicConfig(
    filename="price_tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Price checked: $99.99")
logging.warning("Price above target")
logging.error("Failed to fetch page")
```

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Config** | Hardcoded + env vars mixed | `@dataclass Config` from env vars |
| **Email** | Basic `sendmail()` | MIME multipart with proper headers |
| **Price parsing** | Single selector | Multiple fallback selectors with `**` |
| **Error handling** | `raise_for_status()` only | Retry logic + exception handling |
| **Logging** | Print only | Timestamped log file |
| **Security** | Basic env vars | Validated config, no hardcoded secrets |
| **String cleaning** | Manual loop | Could use regex or translate |

### Why Production is Better
- **Resilience:** Retry logic and multiple price selectors handle site variations
- **Security:** All credentials from environment variables, proper MIME emails
- **Observability:** Persistent log file for tracking price history
- **Maintainability:** `@dataclass` Config is self-documenting and type-safe
- **Email quality:** MIME format with proper From/To/Subject headers
- **Extensibility:** Fallback selectors adapt to changing page structures

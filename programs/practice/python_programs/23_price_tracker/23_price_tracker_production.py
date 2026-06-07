"""
Price Tracker - Production Version
=====================================

WHAT THIS PROGRAM DOES (Flow):
1. Load configuration from environment variables
2. Validate all required settings are present
3. Fetch product page with retry logic and proper headers
4. Parse HTML to extract current price
5. Compare with target price
6. If price <= target:
   a. Compose email with product details
   b. Send via SMTP with TLS
   c. Log the notification
7. Log all operations with timestamps
8. Display price check summary

INPUTS:
- Environment variables:
  - SMTP_SERVER: SMTP server address (default: smtp.gmail.com)
  - SMTP_PORT: SMTP port (default: 587)
  - EMAIL_ADDRESS: Sender email address
  - EMAIL_PASSWORD: Sender email password or app password
  - RECIPIENT_EMAIL: Recipient email (defaults to sender)
  - PRODUCT_URL: URL of the product to track
  - TARGET_PRICE: Price threshold for notification

OUTPUTS:
- Console: price check results and status
- Email notification when price <= target
- price_tracker_log.txt: detailed operation log (file)

SIDE EFFECTS:
- HTTP request to external website
- SMTP email send (conditional)
- Writes log file to disk

RULES:
- Email sent only when price <= target
- SMTP with TLS encryption required
- Retry up to 3 times on network failure
- All credentials via environment variables (never hardcoded)

ASSUMPTIONS:
- Internet connection available
- Target site accessible and price element parseable
- Email server supports SMTP + TLS
- Environment variables properly configured

DEPENDENCIES:
- requests (pip install requests)
- beautifulsoup4 (pip install beautifulsoup4)
- smtplib (standard library)
- email.mime (standard library)
"""

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

SCRIPT_DIR = Path(__file__).parent.resolve()
LOG_PATH = SCRIPT_DIR / "price_tracker_log.txt"

MAX_RETRIES = 3
TIMEOUT = 15
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0")


@dataclass
class Config:
    """Application configuration loaded from environment variables.

    Attributes:
        smtp_server: SMTP server address.
        smtp_port: SMTP server port.
        email_address: Sender email.
        email_password: Sender password/app password.
        recipient_email: Notification recipient email.
        product_url: URL of the product to track.
        target_price: Price threshold for notification.
    """
    smtp_server: str
    smtp_port: int
    email_address: str
    email_password: str
    recipient_email: str
    product_url: str
    target_price: float


def load_config() -> Optional[Config]:
    """Load and validate configuration from environment variables.

    Returns:
        Config object, or None if required variables missing.
    """
    product_url = os.environ.get("PRODUCT_URL", "https://appbrewery.github.io/instant_pot/")
    target_price_str = os.environ.get("TARGET_PRICE", "100.00")
    email_address = os.environ.get("EMAIL_ADDRESS", "")
    email_password = os.environ.get("EMAIL_PASSWORD", "")

    try:
        target_price = float(target_price_str)
    except ValueError:
        print(f"  Error: TARGET_PRICE '{target_price_str}' is not a valid number.")
        return None

    return Config(
        smtp_server=os.environ.get("SMTP_SERVER", "smtp.gmail.com"),
        smtp_port=int(os.environ.get("SMTP_PORT", "587")),
        email_address=email_address,
        email_password=email_password,
        recipient_email=os.environ.get("RECIPIENT_EMAIL", email_address),
        product_url=product_url,
        target_price=target_price,
    )


def log(message: str, log_lines: list[str]) -> None:
    """Print and store a timestamped log message.

    Args:
        message: Log message.
        log_lines: List collecting all log entries.
    """
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{ts}] {message}"
    print(f"  {message}")
    log_lines.append(entry)


def fetch_page(url: str, log_lines: list[str]) -> Optional[str]:
    """Fetch a webpage with retry logic.

    Args:
        url: Target URL.
        log_lines: Log list.

    Returns:
        HTML string, or None on failure.
    """
    headers = {"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            log(f"Fetching page (attempt {attempt}/{MAX_RETRIES})...", log_lines)
            resp = requests.get(url, headers=headers, timeout=TIMEOUT)
            resp.raise_for_status()
            log(f"OK: HTTP {resp.status_code}, {len(resp.text)} chars", log_lines)
            return resp.text
        except requests.RequestException as e:
            log(f"Error: {e}", log_lines)
            if attempt < MAX_RETRIES:
                time.sleep(attempt * 2)
    return None


def extract_price(html: str, log_lines: list[str]) -> Optional[float]:
    """Extract the product price from HTML.

    Args:
        html: Raw HTML content.
        log_lines: Log list.

    Returns:
        Price as float, or None if not found.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Try multiple common selectors
    selectors = [
        {"id": "priceblock_ourprice"},
        {"class_": "a-price-whole"},
        {"class_": "price"},
        {"class_": "product-price"},
    ]
    price_tag = None
    for selector in selectors:
        price_tag = soup.find(**selector)
        if price_tag:
            log(f"Found price element with selector: {selector}", log_lines)
            break

    if price_tag is None:
        log("Could not find price element on page.", log_lines)
        return None

    price_text = price_tag.getText().strip()
    # Clean price string
    cleaned = ""
    for ch in price_text:
        if ch.isdigit() or ch == ".":
            cleaned += ch
    if not cleaned:
        log(f"Could not parse price from text: '{price_text}'", log_lines)
        return None

    try:
        price = float(cleaned)
        log(f"Extracted price: ${price:.2f}", log_lines)
        return price
    except ValueError:
        log(f"Invalid price value: '{cleaned}'", log_lines)
        return None


def send_notification(config: Config, current_price: float,
                      log_lines: list[str]) -> bool:
    """Send email notification about price drop.

    Args:
        config: Application configuration.
        current_price: The current product price.
        log_lines: Log list.

    Returns:
        True if email sent successfully.
    """
    if not config.email_address or not config.email_password:
        log("Email credentials not configured. Skipping notification.", log_lines)
        return False

    msg = MIMEMultipart()
    msg["From"] = config.email_address
    msg["To"] = config.recipient_email
    msg["Subject"] = f"Price Alert: ${current_price:.2f} (Target: ${config.target_price:.2f})"

    body = (
        f"Price Drop Alert!\n\n"
        f"Current Price: ${current_price:.2f}\n"
        f"Target Price:  ${config.target_price:.2f}\n"
        f"Savings:       ${config.target_price - current_price:.2f}\n\n"
        f"Product URL: {config.product_url}\n\n"
        f"Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    msg.attach(MIMEText(body, "plain"))

    try:
        log(f"Sending email to {config.recipient_email}...", log_lines)
        with smtplib.SMTP(config.smtp_server, config.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(config.email_address, config.email_password)
            smtp.send_message(msg)
        log("Email sent successfully!", log_lines)
        return True
    except smtplib.SMTPException as e:
        log(f"Email send failed: {e}", log_lines)
        return False


def save_log(log_lines: list[str]) -> None:
    """Append log entries to log file.

    Args:
        log_lines: List of log entries.
    """
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n\n")


def run() -> None:
    """Main program entry."""
    print("=" * 40)
    print("       Price Tracker")
    print("=" * 40)
    print()

    log_lines: list[str] = []
    log("Price tracker started.", log_lines)

    config = load_config()
    if config is None:
        log("Configuration error. Exiting.", log_lines)
        save_log(log_lines)
        return

    log(f"Product: {config.product_url}", log_lines)
    log(f"Target:  ${config.target_price:.2f}", log_lines)

    html = fetch_page(config.product_url, log_lines)
    if html is None:
        log("Failed to fetch page. Exiting.", log_lines)
        save_log(log_lines)
        return

    price = extract_price(html, log_lines)
    if price is None:
        log("Could not determine price. Exiting.", log_lines)
        save_log(log_lines)
        return

    print(f"\n--- Price Check ---")
    print(f"  Current: ${price:.2f}")
    print(f"  Target:  ${config.target_price:.2f}")

    if price <= config.target_price:
        diff = config.target_price - price
        print(f"  Status:  BELOW TARGET by ${diff:.2f}!")
        log(f"Price ${price:.2f} is at/below target ${config.target_price:.2f}", log_lines)
        send_notification(config, price, log_lines)
    else:
        diff = price - config.target_price
        print(f"  Status:  ${diff:.2f} above target.")
        log(f"Price ${price:.2f} is above target by ${diff:.2f}", log_lines)

    print(f"-------------------\n")

    log("Price check complete.", log_lines)
    save_log(log_lines)


if __name__ == "__main__":
    run()

"""
Price Tracker - Simple Version
================================

WHAT THIS PROGRAM DOES (Flow):
1. Define target product URL and target price
2. Send HTTP GET request with headers to product page
3. Parse HTML with BeautifulSoup to extract current price
4. Compare current price with target price
5. If price <= target → send email notification
6. Print price check result

INPUTS:
- Environment variables: SMTP_SERVER, EMAIL_ADDRESS, EMAIL_PASSWORD
- Configuration: TARGET_PRICE, PRODUCT_URL (hardcoded)

OUTPUTS:
- Console: current price and comparison result
- Email notification if price is at or below target

SIDE EFFECTS:
- Makes HTTP request to external website
- Sends email via SMTP (if price condition met)

RULES:
- Email sent only when price <= target
- SMTP with TLS encryption
- Uses environment variables for credentials

ASSUMPTIONS:
- Internet connection available
- Target website accessible
- Email server supports SMTP with TLS
- Environment variables configured

DEPENDENCIES:
- requests (pip install requests)
- beautifulsoup4 (pip install beautifulsoup4)
- smtplib (standard library)
- os (standard library)
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import os

# Configuration
PRODUCT_URL = "https://appbrewery.github.io/instant_pot/"
TARGET_PRICE = 100.00

# Email settings from environment
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = 587
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS", "")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL", EMAIL_ADDRESS)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


def get_price():
    """Fetch and parse the product price from the webpage."""
    response = requests.get(PRODUCT_URL, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Adjust selector based on actual website structure
    price_tag = soup.find(id="priceblock_ourprice")
    if price_tag is None:
        price_tag = soup.find(class_="a-price-whole")
    if price_tag is None:
        print("Could not find price element on page.")
        return None

    price_text = price_tag.getText().strip()
    # Remove currency symbols and commas
    price_text = price_text.replace("$", "").replace(",", "")
    return float(price_text)


def send_email(current_price):
    """Send email notification about the price drop."""
    subject = "Price Alert! Price has dropped!"
    body = (f"The price has dropped to ${current_price:.2f}!\n"
            f"Target was ${TARGET_PRICE:.2f}.\n"
            f"Link: {PRODUCT_URL}")
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, message)

    print("Email notification sent!")


# Main
current_price = get_price()
if current_price is not None:
    print(f"Current price: ${current_price:.2f}")
    print(f"Target price:  ${TARGET_PRICE:.2f}")

    if current_price <= TARGET_PRICE:
        print("Price is at or below target!")
        if EMAIL_ADDRESS and EMAIL_PASSWORD:
            send_email(current_price)
        else:
            print("Email credentials not set. Skipping email notification.")
    else:
        print(f"Price is ${current_price - TARGET_PRICE:.2f} above target.")

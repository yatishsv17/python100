# Add On Concepts

- [Create You own ASCII Art](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) . ASCII ART should be inside 3 single quotes opening and close inside print()
- [OpenTriviaDB](https://opentdb.com/) : Database of MCQ's and Quiz Questions

## Sending Emails

```python
# Simple Mail Transfer Protocol
# Import the smtplib module to send emails using SMTP
import smtplib

# Define the sender's email and password (use a Google App Password for security)
my_email = "yatishsv17@gmail.com"
password = "my_google_app_password"

def send_email(to_email, subject, body):
    """
    Send an email using SMTP.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body.

    Returns:
        None
    """
    # Create an SMTP connection to the Gmail server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Enable Transport Layer Security (TLS) to make the connection secure
        connection.starttls()
        # Log in to the sender's email account
        connection.login(user=my_email, password=password)
        # Send the email
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}"
        )

# Example usage
send_email("yatishsv@yahoo.com", "Hello", "This is the body of the email !!!")

```

### Sending SMS

```python
# Import the Client class from Twilio's REST library
from twilio.rest import Client

# Define account_sid and auth_token variables with placeholder values
account_sid = "account_sid"  # Replace with your Twilio account SID
auth_token = "auth_token"  # Replace with your Twilio auth token

# Create a new Twilio client object with the account SID and auth token
client = Client(account_sid, auth_token)

# Define a function to send a message using the Twilio client
def send_twilio_message():
    """
    Send a message using the Twilio client.

    Returns:
        The message SID and status.
    """
    # Create a new message with the Twilio client
    message = client.messages.create(
        body="Hello from Twilio",  # The body of the message
        from_="+16812216234387",  # The Twilio phone number to send from
        to="+917026824563434"  # The phone number to send to
    )
    # Print the message SID and status
    print(message.sid, message.status)

# Call the send_twilio_message function
send_twilio_message()

```

## Website Scraping with BeautifulSoup

```python
from bs4 import BeautifulSoup
import requests

with open("website.html") as file:
   contents=file.read()
#Entire soup object
soup=BeautifulSoup(contents,"html.parser")

# Website Scraping with BeautifulSoup
response=requests.get("Website_URL")
web_page=response.text
# Create a BeautifulSoup object and specify the parser
soup=BeautifulSoup(web_page,"html.parser")

#Prettified version
pretty=soup.prettify()

#Get the title
title=soup.title
title_name=soup.title.name
title_string=soup.title.string

#Get first anchor tag
anchor=soup.a
#Get all anchor tags
anchors=soup.find_all(name="a")
#Only get texts from anchor tags
for tag in anchors:
   print(tag.getText())
#only get href from anchor tags, #tag.get("attribute_name") retrieves attribute value
for tag in anchors:
   print(tag.get("href"))


#get anchor tag inside p tag using selector
first_paragraph=soup.select_one(selector="p a")
#get all anchor tags with class using selector
anchors=soup.select(selector=".anchor")
#get all anchor tags with id using selector
anchors=soup.select(selector="#name")
#get all anchor tags with class and id using selector
anchors=soup.select(selector=".anchor#name")
#get all anchor tags with id and class using selector
anchors=soup.select(selector="#name .anchor")

#get first paragraph
first_paragraph=soup.find(name="p")
#get all paragraphs
paragraphs=soup.find_all(name="p")

#get first heading
heading=soup.find(name="h1")
#get specific heading with id
heading=soup.find(name="h1",id="name")
#get all headings
headings=soup.find_all(name="h1")
#get heading with class
heading=soup.find(name="h3",class_="heading")
```

## Web Scraping with Selenium

```python
# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver with experimental options
chrome_options = webdriver.ChromeOptions()
# Add the detach option to keep the browser window open after the script finishes
chrome_options.add_experimental_option("detach", True)

# Create a new instance of the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Define the URL to navigate to
url = "https://www.python.org/"

# Navigate to the specified URL
driver.get(url)

# Define a section to retrieve elements by different attributes
# Getting the Data by different attributes

"""
The following section demonstrates how to retrieve elements using different attributes.
Each attribute is used to locate a specific element on the webpage.
"""

# Retrieve an element by its ID
element_1 = driver.find_element(By.ID, "id")

# Retrieve an element by its NAME attribute
element_2 = driver.find_element(By.NAME, "name")

# Retrieve an element by its XPath (replace double quotes with single quotes)
element_3 = driver.find_element(By.XPATH, "xpath")

# Retrieve an element by its LINK TEXT
element_4 = driver.find_element(By.LINK_TEXT, "link text")

# Retrieve an element by its PARTIAL LINK TEXT
element_5 = driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")

# Retrieve an element by its TAG NAME
element_6 = driver.find_element(By.TAG_NAME, "tag name")

# Retrieve an element by its CLASS NAME
element_7 = driver.find_element(By.CLASS_NAME, "class name")

# Retrieve an element by its CSS SELECTOR
element_8 = driver.find_element(By.CSS_SELECTOR, "css selector")

# Define a section to retrieve attributes/properties from the retrieved elements
# Getting attributes/properties from the retrieved elements

"""
The following section demonstrates how to retrieve attributes and properties from the previously retrieved elements.
"""

# Print the attribute_name attribute of element_1
print(element_1.get_attribute("attribute_name"))

# Print the size of element_2
print(element_2.size)

"""
The following section demonstrates how to retrieve attributes and properties from the listed multiple elements.
"""

# Extract multiple links from the event list using XPath. Instead of find_elements, if you use find_element, you will get only the first element
element_9 = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/section/div[2]/div[2]/div/ul/li/a")
# Print the extracted links
print("Links extracted using XPath:")
for element in element_9:
    print(element.get_attribute("href"))

# Extract  multiple links from the event list using CSS Selector. Instead of find_elements, if you use find_element, you will get only the first element
element_10 = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# Print the extracted links
print("\nLinks extracted using CSS Selector:")
for element in element_10:
    print(element.get_attribute("href"))


# Find the first name, last name, and email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Angela")
last_name.send_keys("Yu")
email.send_keys("angela@email.com")

# Locate the "Sign Up" button. Then click on it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

# Hitting th ENTER key after typing in the search field
search = driver.find_element(By.NAME, value="search")
search.send_keys(Keys.ENTER)

# Close the browser window
driver.close()

# Quit the WebDriver instance
driver.quit()
```

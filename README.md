# 100 Days of Python

### Inheritence


Inheritance allows us to define a class that inherits all the methods and properties from another class.

```python
class Animal:
    def __init(self):
      self.num_eyes = 2
    
    def breathe(self):
      print("Inhale, Exhale.")
      
class Fish(Animal):
    def __init__(self):
      super().__init__()
     
    def breathe(self):
      super().breathe()
      print("Doing this underwater.")
        
    def swim(self):
      print("moving in water")

 ```


# Files, Directories and Paths


```python
file=open("my_file.txt")
contents = file.read()
print(contents)
close("my_file.txt")
 ```
- Auto close using below snippet:-
```python
with open("my_file.txt") as file:
  contents = file.read()
  print(contents)
 ```

- Return all lines in the file, as a list where each line is an item in the list object:-

```python
file = open("demofile.txt", "r")
print(file.readlines())
 ```


- Open in write mode (Deletes all contents and write data from beginning), It creates new file in the name if the file doesnt exist

```python
with open("my_file.txt",mode="w") as file:
  file.write("New Text.")
  contents = file.read()
  print(contents)
 ```
- Open in Append mode (Add data to contents)

```python
with open("my_file.txt",mode="a") as file:
  file.write("\nNew Text.")
  contents = file.read()
  print(contents)
 ```


### FilePaths


- *Add information here*


### Working with csv data (Pandas Dataframes)


```python
import pandas
df = pandas.read_csv("filename.csv")
df_size_in_tuple=df.shape
df_rownumbers_in_int=df.shape(0)
df_columnnumbers_in_int=df.shape(1)
row = df[df.column_name == "column_value"]
row = df[df[column_name] == "column_value"]
element = row.column_name.item()
new_df.to_csv("filename.csv")

"""
ADD A ROW with new name's birthday data by read a csv with NAME as index and updating it 
"""

df = pd.read_csv("birthdays.csv",index_col='name')
df.loc["Yatish_Yahoo"]=["yatishsv@yahoo.com", 2023, 4, 24]
df.to_csv("birthdays.csv")


df = pd.read_csv("data.csv")
new_row = pd.Series({'column_name' : "new value"})
df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
"""Following line avoids adding new indexes"""
df.to_csv("data.csv",index=False)


"""
ADD A COLUMN with addresses to existing birthday data by read a csv with NAME as index and updating it 
"""

df = pd.read_csv("birthdays.csv",index_col='name')
address = ['Delhi', 'Bangalore']
df['Address'] = address
df.to_csv("birthdays.csv")
 ```

- Looping through rows (series) of a data frame: 

```python
    for (index,row) in df.iterrows():
        print(row.column_name)
 ```    


### #Working with Json data (Inbuilt JSON Module)


```python
import json

"""Read Json Data"""

with open("data.json", mode="r") as jsonfile:
    data=json.load(jsonfile)

"""Write Json Data to new File"""

with open("data.json", mode="w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

"""Write Json Data to Existing File : Read existing data --> Update new data to the existing Data --> Rewrite JSON file with updated data"""

with open("data.json", mode="r") as jsonfile:
    data=json.load(jsonfile)
    data.update(new_data)
with open("data.json", mode="w") as jsonfile:
    json.dump(new_data,jsonfile, indent=4)

 ```

- Looping through rows (series) of a data frame: 

```python
    for (index,row) in df.iterrows():
        print(row.column_name)
 ```    


### Creating GUI Programs


```python
    from tkinter import *

    listvar="Not Selected"
    scalevar=0


    #Function for the all Buttons to execute
    def func():
        textbox_text=text.get("1.0", END)
        label.config(text=f"spinbox-value is '{spinbox.get()}'\n"
                        f"Checkbutton-value is '{checked_state.get()}'\n"
                        f"RadioButton-value is '{radio_state.get()}'\n"
                        f"entry-text is '{entry.get()}'\n"
                        f"Textbox-text is '{textbox_text}'\n"
                        f"Selected List Element is '{listvar}''\n"
                        f"Scale Value is '{scale.get()}'")

    # New Window
    window = Tk()
    window.title("Title")
    window.minsize(width=1000, height=1000)
    window.configure(bg="#f7f5dd",padx=50,pady=50)

    #Spinbox
    spinbox = Spinbox(from_=0, to=10, width=5, command=func)
    spinbox.grid(row=0, column=0)

    #Checkbutton
    checked_state = IntVar()
    checkbutton = Checkbutton(text="Checkbutton", variable=checked_state, command=func)
    checkbutton.grid(row=0, column=1)

    #Radiobutton
    #Variable to hold on to which radio button value is checked.
    radio_state = IntVar()
    radiobutton1 = Radiobutton(text="Radio_Button 1", value=1, variable=radio_state, command=func)
    radiobutton2 = Radiobutton(text="Radio_Button 2", value=2, variable=radio_state, command=func)
    radiobutton1.grid(row=0,column=2)
    radiobutton2.grid(row=0,column=3)

    # Entries
    entry = Entry(width=10)
    entry.insert(END,string="Entry text")
    entry.grid(row=1, column=0)

    #Text
    text = Text(height=5, width=30)
    #Puts cursor in textbox.
    text.focus()
    #Adds some text to begin with.
    text.insert(END, "Text with Cursor Focus.")
    text.grid(row=1,column=1)

    #Listbox
    def listbox_func(element):
        global listvar
        listvar=listbox.get(listbox.curselection())
        func()
    listbox = Listbox(height=4)
    List = ["Listbox Element 1", "Listbox Element 2", "Listbox Element 3", "Listbox Element 4"]
    for item in List:
        listbox.insert(List.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_func)
    listbox.grid(row=1,column=2)

    #Scale
    def scale_func(value):
        global scalevar
        scalevar=value
        func()
    #Called with current scale value.
    scale = Scale(from_=0, to=100, command=scale_func)
    scale.grid(row=1,column=3)


    # Button : calls func() when pressed, use state="disabled" to disable the button
    button = Button(width=50,text="Button", command=func,state="normal")
    button.grid(row=2, column=1,columnspan=2)

""" Buttons with image """
    photoimage = PhotoImage(file="./images/right.png")
    rbutton = Button(image=photoimage, highlightthickness=0, command=question_card)
    rbutton.grid(row=2, column=2)


    # Labels
    label = Label(width=50,text="Label", font=("Arial", 12, "bold"), bg="#e2979c")
    label.grid(row=3, column=1,columnspan=2)


    window.mainloop()
 ```


### #Using Canvas

```python
from tkinter import *
timer = None

"""# New Window"""

window = Tk()
window.title("Title")
window.minsize(width=1000, height=1000)
window.configure(bg="#f7f5dd",padx=50,pady=50)

def timer_func():
    count_down(60)

def count_down(seconds):
    global timer
    if seconds>0:
        canvas.itemconfig(timer_text, text=seconds)
        timer = window.after(1000, count_down, seconds-1)

def reset_func():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="Inserted Image")
    seconds=60

"""PhotoImage objects should not be created inside a function. Otherwise, it will not work
Use width to wrap canvas text
"""
# Canvas
canvas = Canvas(width=200, height=224, bg="#9bdeac", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="Inserted Image", width=180,fill="white", font=("Courier", 15, "bold"))
canvas.grid(row=3,column=2)

"""# Button : calls func2() when pressed"""

start_button = Button(text="Start_Timer",command=timer_func)
start_button.grid(row=4, column=2)
reset_button = Button(text="Reset_Timer",command=reset_func)
reset_button.grid(row=5, column=2)

window.mainloop()

 ```


### #Pop Ups : Message boxes


```python

from tkinter import messagebox

"""# Show Error"""

messagebox.showerror(title="Error",message="Error Message") ==> Pop Up an Error

"""# Show Info"""
 
messagebox.showinfo(title="Info", message="Info Message")

"""# Ask OK or Cancel : Pop up for confirmation and save the reply (True or False) into a variable"""
 
is_ok=messagebox.askokcancel(title="Title",message="Entered Details")
 ```


### #Copy to clipboard


```python
"""# Pyperclip needs to be installed"""

import pyperclip

"""# Copy the field email to the clipboard"""

pyperclip.copy(email)

"""# To paste the copied text"""
pyperclip.paste()
 ```

### Catching Exceptions

```python

"""
TRY executes a code block which might cause an exception
Following scenarios are exception raising situations where:
- FileNotFoundError : a_file may not already exist and might raise an exception
- KeyError: trying to access a list value Out of index
"""
try:
    file = open("a_file.txt")
    dict={"key":"value"}
    print(dict["non_existent_key"])

"""
EXCEPT executes a code block when a specific exception is raised by TRY block
We can also capture the error message thrown by an exception by using AS KeyWord
"""
except  FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Some text")

except KeyError as error_message: 
    print(f"Key {error_message}does not exist")


"""
ELSE executes a code block when an exception is not raised by TRY block
"""
else:
    content=file.read()



"""
FINALLY executes the code block irrespective of any exception scenario from TRY block
"""
finally:
    file.close()
    print("File was closed")



"""
RAISE is used to raise our own exceptions.
"""
if human_height > 3:
    raise ValueError("Human height cannot be above 3 meters")

 ```

### Sending Emails
```python
import smtplib

my_email = "yatishsv17@gmail.com"
password="my_google_app_password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="yatishsv@yahoo.com",
        msg="Subject:Hello\n\n "
            "This is the body of email !!!")

 ```

### Sending SMS
```python
from twilio.rest import Client

account_sid = "account_sid"
auth_token = "auth_token"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+16812216287",
  to="+917026824562"
)
print(message.sid,message.status)

 ```

### Getting data using APIs

**API Method** : method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. (POST is for adding new data, PUT is for updating existing data)

```python

import requests

opentb_endpoint="https://opentdb.com/api.php"
parameters = {
    "amount" : 10,
    "type" : "boolean"
}

response=requests.get(url=opentb_endpoint, params=parameters)
response.raise_for_status()
json=response.json()
question_data = json["results"]
print(question_data)
```

- Using API Keys

```python
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "my_api_key"
weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
 ```

 - Post to an API endpoint using Header Authentication : Edit Google Sheet spreadsheet via Sheety API

 ```python

SHEETY_URL="https://api.sheety.co/fb08e2b31067628f811b6d467af12ff2/workoutTracking/workouts"

sheety_header={
'Content-Type':'application/json',
'Authorization':"Auth Token"
}


workout_data={
    "workout": {
	    "date": "07/01/2023",
	    "time": "15:00:00",
        "exercise": "Running",
        "duration": "5.5",
        "calories": "32.5"
  }
}

sheety_response = requests.post(url=SHEETY_URL, json=workout_data, headers=sheety_header)
sheety_response.raise_for_status()
sheety_data = sheety_response.json()
sheety_data2 = sheety_response.text
  ```

### Web Foundation

### #Code Files

- HTML : Responsible for structure of website (Builder, Architect, Engineer of a house)
- CSS : Responsible for style of website (Painter, interior designer of a house)
- JS : Functionalities of the wensite (Electrician, Plumber of a house )

### HTML (HyperText Markup Language)

- Non-Void Elements (Forward Slash at beginning)
    - Headings
    - Paragraphs
- oid Elements (Forward Slash at End)
    - Horizontal Rule
    - Break
### ##Heading Element

< h1 > Hello World < /h1 >

Tags are the entities enclosed inside Angle brackets : < h1 >
Element are entitues enclosed inside open and closed tags : < h1 > Hello World < /h1 >
Maximum number of headings : H6

### ##Paragraph Element

- < p > paragraph < /p >
Generate dummy text/words/paragraphs etc : https://www.lipsum.com/

### ##Horizontal Rule Element

- < hr/ > 

### ##Break Element

- < br/ > 

Comapre Text/Image/PDF/Excel/Folders etc : https://www.diffchecker.com/

### ##Ordered Lists
```
<ol>
    <li> </li>
    <li> </li>
    <li> </li>
</ol>

 ```


### ##Unordered Lists : Bullet points
```
<ul>
    <li> </li>
    <li> </li>
    <li> </li>
</ul>

 ```

### ##Anchor Elements : Attribures- Specified inside opening tags
```
<anchor_tag attribute=value 2nd_attribute=2nd_value>Element body</anchor_tag>
<a href="https://ww.google.com">This is a link </a>

 ```

### ##Images (Void element: Slash at end)
```
<img src="image_URL.com"/ alt="alternative text description">

 ```

**alt** helps visually impaired to understand by using voice text readers

### #HTML Boilerplate

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
	<script src="index.js"></script>
  </body>
</html>
 ```

### CSS : Cascading Style Sheets

### #Adding CSS to HTML
1. Inline : Same line as HTML Element : Target Single element
    ```
    <tag style="css"/>

    <h1 style="background:blue"></h1>
     ```
1. Internal : Targets single webpage
    ```
    html_element_selector{
            background:red;
        }
     ```
    HTML element Selector can be any HTML element : h1,h2,h3,p etc,

    ```
    <style>css</style>


    <head>
    <style>
        html{
            background:red;
        }
    </style>
    </head>
     ```
1. External : Target Multipage Website
    ```
    <html>
    <head>
    <link rel="stylesheet" href="style.css"/>
    </head>
    </html>
     ```

### #CSS Selectors

Heirarchy / Priority

Universal Selectors > attributes and values selectors > ID selectors > Class selectors > HTML Element Selectors

```

p{
  color:red
}

<p >1. The element selector targets elements based on their HTML tag name.</p>


.class-name{
  font-size: 20px
}

<ol>
<li class="class-name" value="2">Class selectors target elements based on the value of the class attribute.</li>
</ol>


#id-name{
  color: green;
}

<ol>
<li class="note" id="id-name" value="3">ID selectors target elements based on the value of the id
      attribute. ID's are unique to a webpage, classes aren't.</li>
</ol>



li[value="4"]{
  color: blue;
}

<ol>
<li class="note" value="4">Attribute selectors target elements based on their attributes and values.</li>
</ol>


*{
  text-align: center
}


<ol>
<li class="note" value="5">The universal selector targets all elements.</li>
  </ol>
 ```
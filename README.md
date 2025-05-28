# 100 Days of Python

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

### Getting data using APIs

- APIs : Application Programming Interface
- Status Codes:
- - 1XX : Informational / Hold on
- - 2XX : Success
- - 3XX : Redirection / Go Away
- - 4XX : Client Error / You Screwed Up
- - 5XX : Server Error / Server Down / I(server) screwed Up
    **API Method** : method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. (POST is for adding new data, PUT is for updating existing data)
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
#Raise an exception if 200 is not returned
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

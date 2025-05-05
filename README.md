# 100 Days of Python


## Python Notes


- PEMDAS: Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)
- Flow division : ```8//3``` : gives quotient
- Mod : ```8%3``` : gives reminder
- Exponent : ```5**2``` : answer 25
- ```a=a+1```  is equal to ```a += 1```
- f-string : ```print(f"Score is {score_var}")```
- ```type()``` gives datatype, ```int(),float(),str()``` used to change datatype
- ```len()``` gives character length of a string
- Always finalise flow charts before starting to code for conditional statements.
- Use IF_ELIF_ELSE for OR condition, Multiple IFs for AND condition
- [Create You own ASCII Art](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) . ASCII ART should be inside 3 single quotes opening and close inside print()
- [OpenTriviaDB](https://opentdb.com/) : Database of MCQ's and Quiz Questions
- Python uses Mersenne Twister pseudorandom number generator (PRNG) for randomization
    - [Khan Academy on Mersenne Twister ](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)
- [Ask Python ](https://www.askpython.com/)
- PASSing the loop for specific condition
```python
i=0
while (i<10):
    i+=1
    pass

 ```


## Debugging


- Describe Problem
- Reproduce the Bug
- Play Computer
- Fix the Errors from console
- Print is Your Friend
- Use Debuggers like [Thonny](https://thonny.org/) or [PythonTutor](https://pythontutor.com/) : Step-by-step expression evaluation, detailed visualization of the call stack and a mode for explaining the concepts of references and heap
- Take a break
- Ask a real human friend
- Run often
- Ask Stackoverflow


## Lists


- Lists to store information of related data like countries, states ordered by criteria like alphabetical, population etc.
- ```list1.append("Value_to_be_Appended")``` : Append adds one more element to existing list
- ```list1.extend(["Value1,Value2,Value3]")``` : Extend appends a new list to existing list
- ```list1[-1]=value``` updates existing value, ```list1.append("value")``` adds new value
- Empty list : ```list2=[]```
- [Python Datastructures](https://docs.python.org/3/tutorial/datastructures.html#)
- Loop through list
```for value in list1:```
- Loop through each letter of word
```for letter in chose_word:```
- Loop through position of letters of a word
```for position in range(len(chosen_word))```
- Nesting list:
    ```l1=[[l2],[l3]]```
    ```l1[index1][index2]```

- Splitting

```python

txt = "Line, that neeeds to be split for every , (comma)"
x = txt.split(", ")
print(x)

Answer: "Result : ['Line', 'that neeeds to be split for every ', '(comma)']"
 ```

- Slicing

```python 

list[2:5]      ==> Include list[2] till list[4], excludes list[5] 
list[2:]       ==> All starting from list[2]
list[:5]       ==> All till list[5]
list[2:5:2]    ==> Slice from 2 to 5 in increments of 2
list[::1]      ==> List with alternative elements
list[::-1]     ==> Reverse the list

 ```

- Replace : replace a substring inside a string. Replace doesnt alter existing variable contaning the string, you need to explicitly save it to a variable.

```python
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
 ```

- Stripping : remove forward and backwards spaces by default. Else, strip specified characters from remove forward and backwards of the string

```python
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

Answer : banana

txt = ",,,,,rrttgg.....bangrtana....rrr"
x = txt.strip(",.grt")
print(x)

Answer : "bangrtana"
 ```

- Joining elements in a list

```python
myList = ["John", "Peter", "Vicky"]
x = "#".join(myList)
print(x)
Answer : "John#Peter#Vicky"
 ```

- Joining two lists

    ```list=list1+list2```


### List Comprehension


- new_list=[**new_item** for **item** in **list** if **condition**]


## Dictionaries 


```python
    d1=
        {
        "key1":"Value1",
        "key2":"Value2",
        "key3":"value3",
        }
 ```

- Retrieving value from dictionary: ```d1["key1"]``` or ```d1.get("key1)``` (This return null if key is not available, former returns error)
- Append/Update a KV Pair: ```d1["key4"]="value4"```
- empty dictionary : ```d2={}```
- Looping through: 

   ```python
    for key in d1:
        print(key:d1[key])

    for (key,value) in d1.items():
        print(value)
    ``` 

- Nesting dictionary with both list and key

   ```python
    d1={
        key1:[],
        key2:{}
    }
     ```


### Dictionaries Comprehension


- Create dictionary from a list 

    - new_dict={**new_key:new_value** for **item** in **list**}

- Create dictionary from a dictionary

    - new_dict={**new_key:new_value** for **(key, value)** in **dict.items()** if **condition**}


## Functions : 


- Bundle set of steps to achieve a functionality 
    - x and y are **parameters** and 5,8 are **arguments**

       ```python
        def function1(x,y):
            do a,b,c with x,y
            return result

        function1(5,8)
        ```
    
    - x and y are **Default value parameters**

       ```python
        def function1(x=1,y=2,z):
            do a,b,c with x,y,z
            return result

        function1(x=10,z=3)
        ```
    - Function with **Unlimited positional arguments** . Arguments are stored in tuple

       ```python
        def add(*args):
            for n in args:
                do operation on n
            return result

        function1(x=10,z=3)
        ```
    - Function with **Unlimited keyword arguments** . Arguments are stored in dictionary

       ```python
        def add(**kwargs):
            for key,value in kargs.items():
                do operation on n
            return result

        function1(x=10,z=3)
        ```
    - Function with hints and Arrows

       ```python
       """ function hints only integer dataType arguments are allowed and also says function returns bool"""
        def func(a : int) -> bool:
            if a >10:
                return True
            else:
                return False

        ```

- ```return``` will exit the function and prevent the rest of the code from being executed.
- Make use of ```print()``` function to debug infinite loops
- **docstring** : ```""" Write multiline docstrings inside triple double-quotes """``` . Docstrings says what function intends to do and return
- ``lower()``` converts string to lowercase, ```upper()``` converts to Uppercase```, ```title()``` converts to Titlecase```, ```count()``` counts occurrence of a character in a string
- String format() : Following returns 49.00 dollars
   ```python
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price = 49))
    ```
- **High Order Function**: Function which takes other functions as parameters

   ```python
    def func1(n1,n2):
        return n1*n2

    def func2(n1,n2):
        return n1+n2
    
    #func3 is High Order Function
    def func3(n1,n2,func)
        return func(n1,n2)
    ```

## Namespace: 


- Global Scope variables and functions (Not Parameters/Arguments) are available even inside the functions where that variable/function is not defined whereas local scope variables and functions that are defined inside of a function are available only inside the function and are not visible at global kevel.
- Python doesnt have block scopes i.e new variables that are defined inside blocks like if, while and for loops are accessible outside the blocks (They arent accessible in C and C++, they do have block scopes).
- Use keyword **global** to access a global variable inside functions. Avoid using this method.


## Modules

- Module : A file containing Python code, definitions of functions, statements, or classes used for executing specific functionalities
    - Increase the upper limit of ```random.random()``` from 1 to x by multiplying by x


- Import module from python standard libraries

   ```python
    import module_name
    from module_name import Class/Function
    from module_name import *
    import module_name as t
    ```

- Import other modules : pypi.com

   ```python
    # Install Package
    pip install package_name
    import module_name
    ```

- datetime module

```python

import datetime as dt

now = dt.datetime.now()
print(now.day,now.month,now.year)
print(now.strftime("%Y%m%d"))

 ```


## OOP : Object Oriented Programming


- **Class** is like a blueprint, **Object** is like a product made out of blueprint.
- ```object_name=module_name.ClassName()``` Declaring object when module is imported  into the file.
- ```object_name=ClassName() ``` Declaring object when class is imported directly into the file.
- ```object_name.attribute_name``` Accessing an attribute of the object. Attributes are like variables, you can change their value to change the style and appearances
- ```object_name.module_name(arguments)``` Accessing a method of the object. Methods are like functions, they take in arguments and process different functionalities to them
- [Python library](https://docs.python.org/3/library/) for Classess
- [Python Packages](https://pypi.org/) : The Python Package Index (PyPI) is a repository of software for the Python programming language
    - install the package
    - import the module
    - Use the class
- Creating a class: ```Class ClassName:``` Class Name should be in PascalCase
- Use ```pass``` to create empty class
- Constructor is part of Class which helps in initialising with starting values
    - ```def __init__(self)``` : This function is called everytime object is created. Attributes that mandatorily needs to be passed will be parameters of init function, default or optional attributes can be defined inside init, though not passed as parameters.
    - New attributes can also be added directly to the objects, jult like adding extras to your new car which came out of a blueprint 

   ```python
        class ClassName:
            def __init__(self,param1,param2):
                self.attr1=param1
                self.attr2=param2
                self.attr3=0
                self.attr4=defaultValue

            def method_name(self,param1):
                self.attr5 += 1
                param1.attr6 +=1

        object_name=ClassName(arg1,arg2)
        print(object_name.attr1,object_name.attr2,object_name.attr3,object_name.attr4)
    ```

    Example:-

   ```python
        class InstagramUser:

            def __init__(self,user_id,username):
                self.id = user_id
                self.username = username
                self.followers = 0
                self.following = 0

            def follow(self,user):
                user.followers += 1
                self.following += 1

        user1=InstagramUser(1288,"y4yatish")
        user2=InstagramUser(8383,"yatishfilms")
        user1.follow(user2)

        print(user1.username,user1.followers,user2.username,user2.followers)
    ```

- Instances are the objects created from same class, but have different attribute values(color,shape,speed etc) 


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

### Working with Json data (Inbuilt JSON Module)


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


## Creating GUI Programs


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


### Using Canvas

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


### Pop Ups : Message boxes


```python

from tkinter import messagebox

"""# Show Error"""

messagebox.showerror(title="Error",message="Error Message") ==> Pop Up an Error

"""# Show Info"""
 
messagebox.showinfo(title="Info", message="Info Message")

"""# Ask OK or Cancel : Pop up for confirmation and save the reply (True or False) into a variable"""
 
is_ok=messagebox.askokcancel(title="Title",message="Entered Details")
 ```


### Copy to clipboard


```python
"""# Pyperclip needs to be installed"""

import pyperclip

"""# Copy the field email to the clipboard"""

pyperclip.copy(email)

"""# To paste the copied text"""
pyperclip.paste()
 ```

## Catching Exceptions

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

## Sending Emails
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

## Sending SMS
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

## Getting data using APIs

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

## Web Foundation

### Code Files

- HTML : Responsible for structure of website (Builder, Architect, Engineer of a house)
- CSS : Responsible for style of website (Painter, interior designer of a house)
- JS : Functionalities of the wensite (Electrician, Plumber of a house )

## HTML (HyperText Markup Language)

- Non-Void Elements (Forward Slash at beginning)
    - Headings
    - Paragraphs
- oid Elements (Forward Slash at End)
    - Horizontal Rule
    - Break
#### Heading Element

< h1 > Hello World < /h1 >

Tags are the entities enclosed inside Angle brackets : < h1 >
Element are entitues enclosed inside open and closed tags : < h1 > Hello World < /h1 >
Maximum number of headings : H6

#### Paragraph Element

- < p > paragraph < /p >
Generate dummy text/words/paragraphs etc : https://www.lipsum.com/

#### Horizontal Rule Element

- < hr/ > 

#### Break Element

- < br/ > 

Comapre Text/Image/PDF/Excel/Folders etc : https://www.diffchecker.com/

#### Ordered Lists
```
<ol>
    <li> </li>
    <li> </li>
    <li> </li>
</ol>

 ```


#### Unordered Lists : Bullet points
```
<ul>
    <li> </li>
    <li> </li>
    <li> </li>
</ul>

 ```

#### Anchor Elements : Attribures- Specified inside opening tags
```
<anchor_tag attribute=value 2nd_attribute=2nd_value>Element body</anchor_tag>
<a href="https://ww.google.com">This is a link </a>

 ```

#### Images (Void element: Slash at end)
```
<img src="image_URL.com"/ alt="alternative text description">

 ```

**alt** helps visually impaired to understand by using voice text readers

### HTML Boilerplate

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

## CSS : Cascading Style Sheets

### Adding CSS to HTML
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

### CSS Selectors

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
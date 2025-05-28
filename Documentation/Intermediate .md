# Intermediate Level Python Concepts

### OOP : Object Oriented Programming

- **Class** is like a blueprint, **Object** is like a product made out of blueprint.
- ```object_name=module_name.ClassName()``` Declaring object when module is imported  into the file.
- ```object_name=ClassName() ``` Declaring object when class is imported directly into the file.
- ```object_name.attribute_name``` Accessing an attribute of the object. Attributes are like variables, you can change their value to change the style and appearances
- ```object_name.method_name(arguments)``` Accessing a method of the object. Methods are like functions, they take in arguments and process different functionalities to them
- [Python library](https://docs.python.org/3/library/) for Classess
- [Python Packages](https://pypi.org/) : The Python Package Index (PyPI) is a repository of software for the Python programming language
    - install the package
    - import the module
    - Use the class
- Creating a class: ```Class ClassName:``` Class Name should be in PascalCase
- Use ```pass``` to create empty class
- Constructor is part of Class which helps in initialising with starting values
    - ```def __init__(self)``` : This function is called everytime object is created. Attributes that mandatorily needs to be passed will be parameters of init function, default or optional attributes can be defined inside init, though not passed as parameters.
    - New attributes can also be added directly to the objects, just like adding extras to your new car which came out of a blueprint 

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

- Instances are the objects created from same class, but have different states (attribute values(color,shape,speed etc)  and methods)

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


###  Files, Directories and Paths

- Auto close using below snippet:-
```python
  with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    # Return all lines in the file as a list where each line is an item in the list object
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

- Filepaths
- - Absolute
- - - Access from any location using path from root directory. ```/home/user/Documents/my_file.txt```
- - Relative
- - - Access from current working directory. ```my_file.txt``` or ```./my_file.txt```
- - - Access a directory below current working directory. ```./directory_name/my_file.txt```
- - - Access a parent directory above current working directory. ```../my_file.txt```
- - - Access a  directory inside parent directory viz above current working directory. ```../directory_name/my_file.txt```    

### Working with csv data (Pandas Dataframes)

- Table is equavalent to Dataframe object (Equivalent to dictionary in Python)
- Column / row is equivalent to Series object (Equivalent to list in Python)
- ```dataframe_name[column_name]``` to access a column
- ```dataframe_name[dataframe_name[column_name]==cell_value]``` to access the row containing the cell value
- ```dataframe_name[dataframe_name.column_name == cell_value]``` to access the row containing the cell value
- Interate through rows (series) of a data frame: ```for (index,row) in dataframe_name.iterrows():```

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


# Looping through rows (series) of a data frame: 

for (index,row) in df.iterrows():
    print(row.column_name)
  

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

#json.load() converts json data to python dictionary
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


### Error Handling and Catching Exceptions
- try : executes a code block which might cause an exception
- except: executes a code block when a specific exception is raised by TRY block
- else: executes a code block when an exception is not raised by TRY block
- finally: executes the code block irrespective of any exception scenario from TRY block

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
#Simple Mail Transfer Protocol
import smtplib

my_email = "yatishsv17@gmail.com"
password="my_google_app_password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    #TLS : Transport layer security. make connection secure
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

### Using environment variables

- n python Terminal : export TWILIO_ACCOUNT_SID = "account_sid" and TWILIO_AUTH_TOKEN = "auth_token"
- Using saved environment variables in python file
```python
import os
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
```
- To run python file from terminal/cloud ```export TWILIO_ACCOUNT_SID = "account_sid" ; TWILIO_AUTH_TOKEN = "auth_token"; python3 main.py```
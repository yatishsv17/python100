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


# Python 100 - Beginner

### DataTypes and String Manipulators

- PEMDAS: Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)
- `6/3` : gives float output : Implicit type casting returns float even though result is whole number, Division always gives float output
- f-string : `print(f"Score is {score_var}")`. instead of concatenating strings with variables, use f-string for better readability. Example : `"first_name"+" "+ "last_name"` can be written as `f"{first_name} {last_name}"`
- `.format()` method for string formatting.  Fills in the {placeholders} with actual values
  - `name = "The {} {}".format("Mumbai", "Tiger")`
  - `name = "The {city} {pet}".format(city="Mumbai", pet="Tiger")`

- Maths
  - 3+2 Add
  - 4-1 Subtract
  - 2\*3 Multiply
  - 5/2 Divide
  - 5\*\*2 Exponent / Power
  - 5%2 Mod : Gives reminder
  - 5//2 Floor Division : gives quotient which is integer

### Enumerations (enum)

- Enum : A way to create a group of named, fixed constants. Instead of using confusing numbers like 1, 2, 3 scattered throughout your code, you give them meaningful names.Use enums when you have a fixed set of related value like days of week, colors, etc.

```python
from enum import Enum

class Color(Enum):
    RED   = 1
    GREEN = 2
    BLUE  = 3.

print(Color.RED)        # Color.RED
print(Color.RED.name)   # 'RED'
print(Color.RED.value)  # 1
```
- Loop through all members with `for member in Color:`
- No __init__, no arguments passed from outside. The values are written directly inside the class body. Because an Enum is NOT meant to create new objects dynamically. It represents a fixed, closed set of constants that should never change.

### Lists

- `list1.append("Value_to_be_Appended")` : Append adds one more element to existing list
- `list1.extend(["Value1,Value2,Value3]")` : Extend appends a new list to existing list
- Loop through list
  `for value in list1:`
- Loop through each letter of word
  `for letter in chosen_word:`
- Loop through each integer till a number
  `for number in range(1,101):`
- Loop through position of letters of a word
  `for position in range(len(chosen_word))`
- Nesting list:
  `l1=[[l2],[l3]]`
  `l1[index1][index2]`

- Splitting 

```python
txt = "Line, that neeeds to be split for every , (comma)"
x = txt.split(", ")
print(x)
```

- Slicing

```python

list[2:5]     # ==> Include list[2] till list[4], excludes list[5]
list[2:]      # ==> All starting from list[2]
list[:5]      # ==> All till list[5]
list[2:5:2]   # ==> Slice from 2 to 5 in increments of 2
list[::1]     # ==> List with alternative elements
list[::-1]    # ==> Reverse the list

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

```python
list=list1+list2
```

- Answer: "Result : ['Line', 'that neeeds to be split for every ', '(comma)']"

- List Comprehension : To create a new list from an existing list
- - `new_list=[**new_item** for **item** in **list** if **condition**]`

### Dictionaries

- Loop through Dictionary
  ```python
      for key in dict:
          print dict[key]
  ```
- Append/Update a KV Pair: `d1["key4"]="value4"`
- empty dictionary : `d2={}`
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

- Dictionaries Comprehension
- - Create dictionary from a list
    - `new_dict={**new_key:new_value** for **item** in **list**}`

- - Create dictionary from a dictionary
    - `new_dict={**new_key:new_value** for **(key, value)** in **dict.items()** if **condition**}`

### Loops

- `continue` keyword is a loop control statement used to skip the remaining code in the current iteration of a for or while loop. Instead of exiting the loop entirely like the `break` statement, `continue` forces the program to jump immediately to the next iteration

#### While Loop Use Cases

- When you don't know how many times the loop needs to run
- You can just break the loop when a specific condition is not met
- When you need to wait for a condition to be met. Example: waiting for the Right user input like rock, paper, scissors. if the input is not valid, keep asking until it is valid
- When you're processing data until a certain condition is reached

### Functions :

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

  - Function with **Unlimited positional arguments** . Arguments are stored in **tuple**

    ```python
     def add(*args):
         for n in args:
             do operation on n
         return result

     function1(x=10,z=3)
    ```

  - Function with **Unlimited keyword arguments** . Arguments are stored in **dictionary**

    ```python
     def add(**kwargs):
         for key,value in kwargs.items():
             do operation on n
         return result

     function1(x=10,z=3)
    ```

    ````python
    def func(a, *args, **kw):
        print(a, args, kw)

    func(4, 7, 3, 0, x=10, y=64)

    # Output is 4, (7,3,0) {'x':10,'y':64}
    ````

  - Function with hints and Arrows

    ```python
    """ function hints only integer dataType arguments are allowed and also says function returns bool"""
     def func(a : int) -> bool:
         if a >10:
             return True
         else:
             return False

    ```

- `return` will exit the function and prevent the rest of the code from being executed.
- Make use of `print()` function to debug infinite loops
- **docstring** : `""" Write multiline docstrings inside triple double-quotes """` . Docstrings says what function intends to do and return
- ``lower()`converts string to lowercase,`upper()` converts to Uppercase`, `title()` converts to Titlecase`, `count()``` counts occurrence of a character in a string

- String format() : Following returns "For only 49.00 dollars". `.2f` is a format specifier used to format a floating-point number associated with an int variable into a string with exactly two decimal places
  ```python
   txt = "For only {price:.2f} dollars!"
   print(txt.format(price = 49))
  ```
- **Higher Order Function**: Function which takes other functions as parameters

  ```python
   def add(n1,n2):
       return n1*n2

   def substract(n1,n2):
       return n1+n2

   #calculator is High Order Function, dont include function brackets "()" while passing lower order function as argument inside higher order function
   def calculator(n1,n2,func):
       return func(n1,n2)
  ```

### Namespace:

- Global Scope variables and functions (Not Parameters/Arguments) are available even inside the functions whereas local scope variables and functions that are defined inside of a function are available only inside the function and are not visible at global kevel.
- Python doesnt have block scopes i.e new variables that are defined inside blocks like if, while and for loops are accessible outside the blocks (They arent accessible in C and C++, they do have block scopes).
- Use keyword **global** to modify global variable inside functions. Avoid using this method.

### Modules

- Module : A file containing Python code, definitions of functions, statements, or classes used for executing specific functionalities

- Import module from python standard libraries

  ```python
   import module_name
   from module_name import Class/Function
   from module_name import *
   import module_name as t
  ```

- datetime module

  ```python

  import datetime as dt

  now = dt.datetime.now()
  print(now.day,now.month,now.year)
  print(now.strftime("%Y%m%d"))
  ```

- logging module

  - DEBUG → INFO → WARNING → ERROR → CRITICAL

  ```python

  import logging

  logging.basicConfig(
    level    = logging.DEBUG,                            # minimum level to capture
    format   = '%(asctime)s - %(levelname)s - %(message)s',  # message format
    filename = 'app.log',                                # log to file (optional)
    filemode = 'a',                                      # 'a' = append, 'w' = overwrite
    encoding = 'utf-8'                                   # file encoding
  )

  logging.info("This is an info message")
  logging.warning("This is a warning message")
  logging.error("This is an error message")
  logging.critical("This is a critical message")
  ```
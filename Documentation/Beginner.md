
# Day 1 to 14: Beginner

### String manipulation

-  New line : ```\n``` 
-  String concatination : ```"string1"+"string2"```
- For Multi line string, use docstring ```'''<multi-line-string>'''```

### Input Function and Variables
- Save input to a variable : ```name = input("What is your name ?")```
- Length of a string : ```len("string")```

### DataTypes and String Manipulators

- DataTypes : ```type()``` , ```int(),float(),str(),boolean()``` are used to change datatype
- PEMDAS: Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)
- ```6/3``` : gives float output : Implicit type casting returns float even though result is whole number
- Flow division returning integer : ```8//3``` : gives quotient which is integer
- Mod Function : ```8%3``` : gives reminder 
-```round()``` function is used to round off to required decimal numbers.
- Exponent : ```5**2``` : answer 25
- ```a=a+1```  is equal to ```a += 1```
- f-string : ```print(f"Score is {score_var}")```
- ```type()``` gives datatype, ```int(),float(),str()``` used to change datatype
- ```len()``` gives character length of a string
- 

### Conditional Operators

- ```=``` is assignment, ```==`` checks equality in if/elif/else or case or loops checks
- Logical operators : ```and```,```or```and ```not```
- Always finalise flow charts before starting to code for conditional statements.
- Use IF_ELIF_ELSE for OR condition, Multiple IFs for AND condition
- ```import random```, Python uses Mersenne Twister pseudorandom number generator (PRNG) for randomization
    - [Khan Academy on Mersenne Twister ](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)

### Lists

- [Python Datastructures](https://docs.python.org/3/tutorial/datastructures.html#)
- Lists to store information of related data like countries, states ordered by criteria like alphabetical, population etc.
- ```list1.append("Value_to_be_Appended")``` : Append adds one more element to existing list
- ```list1.extend(["Value1,Value2,Value3]")``` : Extend appends a new list to existing list
- [Python Datastructures](https://docs.python.org/3/tutorial/datastructures.html#)
- Loop through list
```for value in list1:```
- Loop through each letter of word
```for letter in chose_word:```
- Loop through each integer till a number
```for number in range(1,101):```
- Loop through position of letters of a word
```for position in range(len(chosen_word))```
- Nesting list:
    ```l1=[[l2],[l3]]```
    ```l1[index1][index2]```
- Passing the loop for specific condition
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
- - ```new_list=[**new_item** for **item** in **list** if **condition**]```

### Dictionaries 

- Loop through Dictionary
    ```python
        for key in dict:
            print dict[key]
    ```
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

- Dictionaries Comprehension
- - Create dictionary from a list 
    - ```new_dict={**new_key:new_value** for **item** in **list**}```

- - Create dictionary from a dictionary
    - ```new_dict={**new_key:new_value** for **(key, value)** in **dict.items()** if **condition**}```

### Loops

```python
i=0
while (i<10):
    i+=1
    pass

 ```


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
            for key,value in kargs.items():
                do operation on n
            return result

        function1(x=10,z=3)
        ```

        ```python
        def func(a, *args, **kw): 
            print(a, args, kw)
 
        func(4, 7, 3, 0, x=10, y=64)

        # Output is 4, (7,3,0) {'x':10,'y':64}
        ```ś
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
- **Higher Order Function**: Function which takes other functions as parameters

   ```python
    def add(n1,n2):
        return n1*n2

    def substract(n1,n2):
        return n1+n2
    
    #calculator is High Order Function, dont include () while passing lower order function as argument inside higher order function
    def calculator(n1,n2,add)
        return func(n1,n2)
    ```

### Namespace: 


- Global Scope variables and functions (Not Parameters/Arguments) are available even inside the functions whereas local scope variables and functions that are defined inside of a function are available only inside the function and are not visible at global kevel.
- Python doesnt have block scopes i.e new variables that are defined inside blocks like if, while and for loops are accessible outside the blocks (They arent accessible in C and C++, they do have block scopes).
- Use keyword **global** to modify global variable inside functions. Avoid using this method.

### Modules

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



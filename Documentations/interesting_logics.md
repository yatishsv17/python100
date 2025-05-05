# Interesting Lgics

## Reborg's World Hurdles Loop Challenge

- Uniform distance and Wall height : 
    - ```turn_right()```
    - ```jump()```
    - ```while not at_goal():```
- Variable distance and Uniform Wall height : 
    - ```while not at_goal():```
        - ```while front_is_clear():```
- Variable distance and Variable Wall height : 
    - ```jump()```
        - ```while not right_is_clear():```
        - ```while front_is_clear():```
    - ```while not at_goal():```
        - ```while front_is_clear():```
        
## Reborg's World Escaping the maze
```python
# Make sure you are at correct starting place with a wall in front
while front_is_clear():
        move()
turn_left() 

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```



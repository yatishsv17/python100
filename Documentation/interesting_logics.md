# Interesting Lgics

## Reborg's World Hurdles Loop Challenge

- Uniform distance and Wall height :
  - `turn_right()`
  - `jump()`
  - `while not at_goal():`
- Variable distance and Uniform Wall height :
  - `while not at_goal():`
    - `while front_is_clear():`
- Variable distance and Variable Wall height :
  - `jump()`
    - `while not right_is_clear():`
    - `while front_is_clear():`
  - `while not at_goal():`
    - `while front_is_clear():`

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

## Caesar Ciper

- Encryption and Decryption of words in a letter by shift position. Use Modulus function to make sure that the encrypted position stays in the range 0 to 25.
  Example : Letter is z and shift_position is 3.

```python
    letter_index=25
    shift_position=3
    final_position=25+3
    # final position is 28
    final_position %= 25
    # final position is 3
    encrypted_letter=alphabets[final_position]
    # encrypted_letter is c
```

## Leap Year

- Years divisible by 4 are leap years.
- However, years divisible by 100 are not leap years, unless
- They are also divisible by 400.

```python
if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
```

## Pomodoro

```python

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)
```

## Turtle Class

- Dashed Line : Use `penup()` and `pendown`
- To draw multiple shapes: exterior angle of a polygon = `360/number_of_sides`
- To draw spirograph : change/add turtle head by `360/no_of_gaps` degrees, and then keep drawing circle `360/no_of_gaps` times

## Math Module

```python
import math
print(math.floor(11/3)) # gives 3 i.e largest whole number less than or equal to number
```

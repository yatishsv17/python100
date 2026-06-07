"""
Treasure Island - Simple Version
=================================

WHAT THIS PROGRAM DOES (Flow):
1. Print welcome message and ASCII art
2. Ask first choice: left or right
   - right → Game Over (fall into a hole)
3. Ask second choice: wait or swim
   - swim → Game Over (attacked by trout)
4. Ask third choice: red, yellow, or blue door
   - red → Game Over (room of fire)
   - blue → Game Over (room of beasts)
   - yellow → You Win! (treasure found)

INPUTS:
- First choice (str): 'left' or 'right'
- Second choice (str): 'wait' or 'swim'
- Third choice (str): 'red', 'yellow', or 'blue'

OUTPUTS:
- Story text and scenario descriptions (console)
- Game Over or Victory message (console)

SIDE EFFECTS:
- None

RULES:
- Winning path: left → wait → yellow
- Wrong choices → immediate game over
- Case-insensitive input

ASSUMPTIONS:
- User understands text adventure format
- Single playthrough per execution

DEPENDENCIES:
- None
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/___/_____/__/_____ --o;   (#)  .; .-"_o.--"_/___/____________/___
/______/___/__/______/_______/  ;--.,   (#)  ._--"o.--"__/_____/___________/___
___/___/___/___/___/____/___/__"=._  ;  (#)  ; .__.-"____/______/___/________/
              |                `"=._o._; ." `"=._o.--"         |
   ___________|_____________________ `"=._o.;""     `"=._o__(__|_______________
              |                                                |
-----------"""""""-----------------------------------------------
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()

        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

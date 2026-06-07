"""
Coffee Machine - Simple Version
=================================

WHAT THIS PROGRAM DOES (Flow):
1. Display menu prompt
2. Accept command: espresso, latte, cappuccino, report, or off
3. If "report" → display current resources
4. If "off" → turn off machine
5. If drink selected:
   a. Check if resources are sufficient
   b. Ask for coin input (quarters, dimes, nickels, pennies)
   c. Calculate total money inserted
   d. Check if money is enough
   e. Dispense drink, deduct resources, add profit, give change

INPUTS:
- Command (str): espresso, latte, cappuccino, report, off
- Coins (int): quarters, dimes, nickels, pennies counts

OUTPUTS:
- Resource report (console)
- Transaction messages (console)
- Drink dispensed message (console)

SIDE EFFECTS:
- Modifies global resource state (water, milk, coffee, money)

RULES:
- Espresso: 50ml water, 18g coffee, $1.50
- Latte: 200ml water, 150ml milk, 24g coffee, $2.50
- Cappuccino: 250ml water, 100ml milk, 24g coffee, $3.00
- Quarter=$0.25, Dime=$0.10, Nickel=$0.05, Penny=$0.01

ASSUMPTIONS:
- Initial resources sufficient for several drinks
- US coin denominations

DEPENDENCIES:
- None
"""

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.00,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)

def make_coffee(drink_name, order_ingredients, cost):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    resources["money"] += cost
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                make_coffee(choice, drink["ingredients"], drink["cost"])
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Invalid choice. Please try again.")

"""
Coffee Machine - Production Version
======================================

WHAT THIS PROGRAM DOES (Flow):
1. Initialize CoffeeMachine with resources and menu
2. Main loop:
   a. Display menu prompt
   b. Accept command (validated)
   c. "report" → display resource report
   d. "off" → shutdown with confirmation
   e. Drink name → process order:
      i.   Check resource availability
      ii.  Prompt for coins (validated, non-negative integers)
      iii. Calculate total money
      iv.  Verify payment covers cost
      v.   Dispense drink, deduct resources, add profit, return change
3. Track order history and total revenue

INPUTS:
- Command (str): espresso, latte, cappuccino, report, off
- Coins (int): non-negative counts for quarters, dimes, nickels, pennies

OUTPUTS:
- Resource report with units (console)
- Transaction details: cost, inserted, change (console)
- Drink dispensed message (console)
- Order statistics on shutdown (console)

SIDE EFFECTS:
- Mutates CoffeeMachine internal state (resources, money, order count)

RULES:
- Espresso: 50ml water, 18g coffee, $1.50
- Latte: 200ml water, 150ml milk, 24g coffee, $2.50
- Cappuccino: 250ml water, 100ml milk, 24g coffee, $3.00
- Quarter=$0.25, Dime=$0.10, Nickel=$0.05, Penny=$0.01

ASSUMPTIONS:
- Initial resources sufficient for several drinks
- US coin denominations, no bills accepted

DEPENDENCIES:
- None (standard library only)
"""

from typing import Optional

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

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

INITIAL_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


class CoffeeMachine:
    """Simulates a coffee machine with resource management and transactions.

    Attributes:
        resources: Current resource levels.
        money: Total profit accumulated.
        orders_served: Number of drinks served.
    """

    def __init__(self) -> None:
        """Initialize the coffee machine with default resources."""
        self.resources = dict(INITIAL_RESOURCES)
        self.money: float = 0.0
        self.orders_served: int = 0

    def report(self) -> None:
        """Display current resource levels."""
        print("\n--- Resource Report ---")
        print(f"  Water:  {self.resources['water']}ml")
        print(f"  Milk:   {self.resources['milk']}ml")
        print(f"  Coffee: {self.resources['coffee']}g")
        print(f"  Money:  ${self.money:.2f}")
        print(f"  Orders: {self.orders_served}")
        print("-----------------------\n")

    def check_resources(self, ingredients: dict[str, int]) -> bool:
        """Check if resources are sufficient for a drink.

        Args:
            ingredients: Required ingredients and amounts.

        Returns:
            True if all resources are sufficient.
        """
        for item, amount in ingredients.items():
            available = self.resources.get(item, 0)
            if amount > available:
                print(f"  Sorry, not enough {item}. "
                      f"(Need {amount}, have {available})")
                return False
        return True

    def process_coins(self) -> Optional[float]:
        """Prompt for coin counts and calculate total.

        Returns:
            Total money inserted, or None on invalid input.
        """
        print("  Please insert coins.")
        total = 0.0
        for coin_name, value in COIN_VALUES.items():
            while True:
                raw = input(f"    How many {coin_name}? ").strip()
                try:
                    count = int(raw)
                except ValueError:
                    print(f"    Error: '{raw}' is not a valid number.")
                    continue
                if count < 0:
                    print("    Error: Cannot insert negative coins.")
                    continue
                total += count * value
                break
        return round(total, 2)

    def make_coffee(self, drink_name: str) -> bool:
        """Attempt to make and serve a drink.

        Args:
            drink_name: Name of the drink from MENU.

        Returns:
            True if drink was successfully served.
        """
        drink = MENU[drink_name]
        ingredients = drink["ingredients"]
        cost = drink["cost"]

        print(f"\n  Processing order: {drink_name.title()} (${cost:.2f})")

        if not self.check_resources(ingredients):
            return False

        payment = self.process_coins()
        if payment is None:
            print("  Error processing coins. Order cancelled.")
            return False

        if payment < cost:
            print(f"  Sorry, ${payment:.2f} is not enough. "
                  f"Need ${cost:.2f}. Money refunded.")
            return False

        change = round(payment - cost, 2)
        if change > 0:
            print(f"  Change: ${change:.2f}")

        for item, amount in ingredients.items():
            self.resources[item] -= amount

        self.money += cost
        self.orders_served += 1

        print(f"  Here is your {drink_name}. Enjoy!\n")
        return True

    def shutdown_summary(self) -> None:
        """Display summary statistics on shutdown."""
        print("\n--- Shutdown Summary ---")
        print(f"  Total orders served: {self.orders_served}")
        print(f"  Total revenue:       ${self.money:.2f}")
        print(f"  Remaining water:     {self.resources['water']}ml")
        print(f"  Remaining milk:      {self.resources['milk']}ml")
        print(f"  Remaining coffee:    {self.resources['coffee']}g")
        print("------------------------")
        print("Coffee machine powered off.\n")


def run() -> None:
    """Main program loop."""
    print("=" * 35)
    print("      Coffee Machine")
    print("=" * 35)
    print()

    machine = CoffeeMachine()
    drink_options = "/".join(MENU.keys())

    while True:
        choice = input(f"What would you like? ({drink_options}): ").strip().lower()

        if choice == "off":
            machine.shutdown_summary()
            break
        elif choice == "report":
            machine.report()
        elif choice in MENU:
            machine.make_coffee(choice)
        else:
            print(f"  Unknown command '{choice}'. "
                  f"Options: {drink_options}, report, off\n")


if __name__ == "__main__":
    run()

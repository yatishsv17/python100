# Coffee Machine - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> while is_on:
        └─> input() → choice
        ├─> "off" → is_on = False
        ├─> "report" → print resources
        ├─> drink name:
        │     ├─> is_resource_sufficient(ingredients)
        │     │     └─> Check each ingredient vs resources
        │     ├─> process_coins()
        │     │     └─> input() × 4 → calculate total
        │     ├─> Check payment >= cost
        │     │     └─> Calculate and return change
        │     └─> make_coffee(name, ingredients, cost)
        │           └─> Deduct resources, add profit
        └─> else → "Invalid choice"
Script End
```

## Production Version Call Flow

### Function Call Graph

```
run()
  ├─> CoffeeMachine()
  │     └─> __init__: resources, money, orders_served
  │
  └─> [Main Loop]
        └─> input() → choice
        ├─> "off" → machine.shutdown_summary()
        │              └─> print() stats and remaining resources
        │
        ├─> "report" → machine.report()
        │                └─> print() all resources and money
        │
        ├─> drink → machine.make_coffee(drink_name)
        │     ├─> machine.check_resources(ingredients)
        │     │     └─> for item, amount in ingredients.items()
        │     │     └─> Compare with self.resources
        │     │
        │     ├─> machine.process_coins()
        │     │     └─> for coin_name, value in COIN_VALUES.items()
        │     │           └─> input() → int() → validate >= 0
        │     │     └─> round(total, 2)
        │     │
        │     ├─> Check payment >= cost
        │     ├─> Deduct ingredients from self.resources
        │     ├─> self.money += cost
        │     └─> self.orders_served += 1
        │
        └─> else → "Unknown command"
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Initialize CoffeeMachine]
    B --> C[Prompt for Command]
    C --> D{Command?}
    D -- off --> E[Shutdown Summary]
    E --> F[End]
    D -- report --> G[Display Resources]
    G --> C
    D -- drink --> H[Check Resources]
    H --> I{Sufficient?}
    I -- No --> J[Show Missing Resource]
    J --> C
    I -- Yes --> K[Process Coins]
    K --> L{Payment >= Cost?}
    L -- No --> M[Refund Money]
    M --> C
    L -- Yes --> N[Calculate Change]
    N --> O[Deduct Resources]
    O --> P[Add Profit]
    P --> Q[Serve Drink]
    Q --> C
    D -- invalid --> R[Show Error]
    R --> C
```

## Class Structure

```mermaid
classDiagram
    class CoffeeMachine {
        -dict resources
        -float money
        -int orders_served
        +__init__()
        +report()
        +check_resources(ingredients) bool
        +process_coins() float
        +make_coffee(drink_name) bool
        +shutdown_summary()
    }

    class MENU {
        espresso
        latte
        cappuccino
    }

    class COIN_VALUES {
        quarters: 0.25
        dimes: 0.10
        nickels: 0.05
        pennies: 0.01
    }

    CoffeeMachine --> MENU : reads recipes
    CoffeeMachine --> COIN_VALUES : reads values
```

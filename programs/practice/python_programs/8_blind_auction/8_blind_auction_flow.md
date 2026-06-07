# Blind Auction - Function Call Flow & Flow Diagram

## Simple Version Call Flow

```
Script Start
  └─> print() welcome
  └─> while continue_bidding:
  │     └─> input() → name
  │     └─> input() → float() → bid
  │     └─> bids[name] = bid
  │     └─> input() → more bidders?
  │     └─> if "yes": os.system(clear)
  │     └─> else: continue_bidding = False
  └─> max(bids, key=bids.get) → winner
  └─> print() winner and amount
Script End
```

## Production Version Call Flow

### Function Call Graph

```
run()
  ├─> print() welcome banner
  ├─> Initialize bids dict
  │
  └─> [Bidding Loop]
        ├─> get_bidder_name()
        │     └─> input().strip()
        │     └─> validate: non-empty, alpha+spaces
        │     └─> .title() for formatting
        │
        ├─> Check duplicate name in bids → warning
        │
        ├─> get_bid_amount()
        │     └─> input().strip() → float()
        │     └─> validate: > 0
        │
        ├─> bids[name] = bid
        │
        └─> input() more bidders?
              ├─> "yes" → clear_screen() → os.system()
              └─> else → break → display_results(bids)

display_results(bids)
  ├─> find_winner(bids)
  │     └─> max(bids, key=bids.get)
  │     └─> return (winner_name, winning_bid)
  └─> Calculate and print statistics
        └─> max(), min(), sum()/len() on bids.values()
```

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Display Banner]
    B --> C[Get Bidder Name]
    C --> D{Valid Name?}
    D -- No --> C
    D -- Yes --> E{Name Already Exists?}
    E -- Yes --> F[Show Overwrite Warning]
    F --> G[Get Bid Amount]
    E -- No --> G
    G --> H{Valid Amount?}
    H -- No --> G
    H -- Yes --> I[Store Bid]
    I --> J{More Bidders?}
    J -- Yes --> K[Clear Screen]
    K --> C
    J -- No --> L{Any Bids?}
    L -- No --> M[Auction Cancelled]
    L -- Yes --> N[Find Winner]
    N --> O[Display Results & Stats]
    O --> P[End]
    M --> P
```

## Auction Data Flow

```mermaid
flowchart LR
    B1["Bid 1: Alice=$100"] --> DICT["bids dict"]
    B2["Bid 2: Bob=$200"] --> DICT
    B3["Bid 3: Carol=$150"] --> DICT
    DICT --> MAX["max(bids, key=bids.get)"]
    MAX --> W["Winner: Bob = $200"]
    DICT --> STATS["Statistics: min, max, avg"]
```

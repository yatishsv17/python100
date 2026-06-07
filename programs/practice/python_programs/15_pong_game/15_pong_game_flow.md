# Pong Game - Function Call Flow & Flow Diagram

## Production Version Call Graph

```
run()
  ├─> Screen setup (title, bgcolor, size, tracer)
  │
  ├─> Paddle(-PADDLE_X)    → Player A (left)
  ├─> Paddle(PADDLE_X)     → Player B (right)
  │     └─> __init__: Turtle(square, white, stretched), goto(x, 0)
  │
  ├─> Ball()
  │     └─> __init__: Turtle(square, white), dx/dy = INITIAL_SPEED
  │
  ├─> Scoreboard()
  │     └─> __init__: score_a=0, score_b=0, writer Turtle, update()
  │
  ├─> draw_center_line(screen)
  │     └─> Turtle → dashed line from top to bottom
  │
  ├─> screen.listen()
  ├─> screen.onkey() × 4 (w, s, Up, Down)
  │
  └─> [Game Loop]
        ├─> screen.update()
        ├─> time.sleep(0.005)
        │
        ├─> ball.move()
        │     └─> setx(xcor + dx), sety(ycor + dy)
        │
        ├─> ball.bounce_walls()
        │     └─> if |ycor| > BOUNDARY_Y → dy *= -1
        │
        ├─> ball.hits_paddle(paddle_b, "right")?
        │     └─> ball.bounce_paddle("right")
        │           ├─> dx *= -1
        │           ├─> speed increase (if < MAX)
        │           └─> setx(COLLISION_X)
        │
        ├─> ball.hits_paddle(paddle_a, "left")?
        │     └─> ball.bounce_paddle("left")
        │
        ├─> ball.past_right()?
        │     └─> scoreboard.point_a() + ball.reset()
        │
        └─> ball.past_left()?
              └─> scoreboard.point_b() + ball.reset()
```

## Mermaid Game Loop

```mermaid
flowchart TD
    A[Game Loop] --> B[screen.update]
    B --> C[ball.move]
    C --> D[ball.bounce_walls]
    D --> E{Hits Paddle B?}
    E -- Yes --> F[ball.bounce_paddle right]
    E -- No --> G{Hits Paddle A?}
    F --> G
    G -- Yes --> H[ball.bounce_paddle left]
    G -- No --> I{Past right?}
    H --> I
    I -- Yes --> J["scoreboard.point_a() + ball.reset()"]
    I -- No --> K{Past left?}
    J --> A
    K -- Yes --> L["scoreboard.point_b() + ball.reset()"]
    K -- No --> A
    L --> A
```

## Class Diagram

```mermaid
classDiagram
    class Paddle {
        -Turtle t
        -int speed
        +__init__(x, color)
        +move_up()
        +move_down()
        +y: float
    }

    class Ball {
        -Turtle t
        -float dx
        -float dy
        +move()
        +bounce_walls()
        +bounce_paddle(side)
        +hits_paddle(paddle, side) bool
        +past_right() bool
        +past_left() bool
        +reset()
    }

    class Scoreboard {
        -int score_a
        -int score_b
        -Turtle writer
        +update()
        +point_a()
        +point_b()
    }

    Ball ..> Paddle : collision check
    Ball ..> Scoreboard : triggers scoring
```

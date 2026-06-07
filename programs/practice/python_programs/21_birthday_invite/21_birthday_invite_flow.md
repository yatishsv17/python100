# Birthday Invite - Page Structure & Flow Diagram

## Simple Version Structure

```
<!DOCTYPE html>
  └─> <html>
        ├─> <head>
        │     └─> <title>
        └─> <body>
              ├─> <h1> Title
              ├─> <h2> Subtitle
              ├─> <img> Cake image
              ├─> <h3> + <ul> Party details
              ├─> <h3> + <p> What to expect
              ├─> <h3> + <p> + <a> RSVP
              ├─> <a> Directions link
              └─> <footer> Closing message
```

## Production Version Structure

```
<!DOCTYPE html>
  └─> <html lang="en">
        ├─> <head>
        │     ├─> <meta charset>
        │     ├─> <meta viewport>
        │     ├─> <title>
        │     └─> <style> (all CSS)
        └─> <body>
              └─> .invitation (card container)
                    ├─> <header>
                    │     ├─> <h1> "You're Invited!"
                    │     └─> <h2> "To My Birthday Party"
                    ├─> .cake-image
                    │     └─> <img> (responsive, object-fit: cover)
                    ├─> <main>
                    │     ├─> .details (bordered card)
                    │     │     └─> <ul> Date, Time, Venue, Dress
                    │     ├─> .section "What to Expect"
                    │     │     └─> <p> Description
                    │     ├─> .section "RSVP"
                    │     │     └─> <a class="rsvp-btn"> mailto link
                    │     └─> .section "Getting There"
                    │           ├─> <address>
                    │           └─> <a class="directions-btn"> maps link
                    └─> <footer>
                          └─> Closing message
```

## Mermaid Page Flow

```mermaid
flowchart TD
    A[Browser Loads Page] --> B[Render HTML Structure]
    B --> C[Apply CSS Styles]
    C --> D[Display Card Layout]
    D --> E{User Interaction}
    E -- Hover RSVP --> F[Button Lift Effect]
    E -- Click RSVP --> G[Open Email Client]
    E -- Hover Directions --> H[Button Lift Effect]
    E -- Click Directions --> I[Open Google Maps]
    E -- Scroll/Read --> J[View Content]
```

## CSS Cascade Structure

```mermaid
flowchart TD
    RESET["* { margin:0, box-sizing }"] --> BODY["body { flex, gradient bg }"]
    BODY --> CARD[".invitation { white bg, shadow, rounded }"]
    CARD --> HEADER["header { gradient, centered text }"]
    CARD --> IMAGE[".cake-image img { responsive, cover }"]
    CARD --> MAIN["main { padding }"]
    MAIN --> DETAILS[".details { purple border-left, light bg }"]
    MAIN --> SECTIONS[".section { margin-bottom }"]
    SECTIONS --> BUTTONS[".rsvp-btn, .directions-btn { gradient, rounded }"]
    BUTTONS --> HOVER[":hover { transform, box-shadow }"]
    CARD --> FOOTER["footer { light bg, italic }"]
```

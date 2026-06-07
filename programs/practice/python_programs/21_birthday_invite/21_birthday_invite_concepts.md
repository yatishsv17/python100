# Birthday Invite - HTML/CSS Concepts

## Core Concepts Used

### 1. Semantic HTML5 Elements
**Concept:** Using meaningful elements instead of generic `<div>` tags.

```html
<header>  <!-- Page/section header -->
<main>    <!-- Main content area -->
<footer>  <!-- Page/section footer -->
<address> <!-- Contact information -->
<nav>     <!-- Navigation links -->
```

| Element | Purpose | Notes |
|---------|---------|-------|
| `<header>` | Introductory content or navigation | Multiple per page OK |
| `<main>` | Primary content | Only **one** per page |
| `<footer>` | Footer content | Multiple per page OK |
| `<section>` | Thematic grouping of content | Should have a heading |
| `<article>` | Self-contained content | Blogs, comments, cards |
| `<address>` | Contact information | Often in `<footer>` |

**Why semantic HTML matters:**
- **SEO:** Search engines understand page structure better
- **Accessibility:** Screen readers announce element roles (e.g., "banner", "main")
- **Maintainability:** Code is self-documenting — `<nav>` vs `<div class="nav">`

### 2. CSS Box Model
**Concept:** Every element is a box with content, padding, border, margin.

```css
* {
    box-sizing: border-box;  /* Include padding/border in width */
}

.invitation {
    max-width: 600px;        /* Content width */
    padding: 30px;           /* Inner space */
    border-radius: 20px;     /* Rounded corners */
    margin: 0 auto;          /* Center horizontally */
}
```

**Box model layers (inside → outside):**
```
┌─────────────── margin ────────────────┐
│  ┌──────────── border ─────────────┐  │
│  │  ┌───────── padding ────────┐   │  │
│  │  │  ┌────── content ─────┐  │   │  │
│  │  │  │                    │  │   │  │
│  │  │  └────────────────────┘  │   │  │
│  │  └──────────────────────────┘   │  │
│  └─────────────────────────────────┘  │
└───────────────────────────────────────┘
```

**`box-sizing: border-box` vs `content-box`:**
```css
/* content-box (default): width = content only */
/* Total width = width + padding + border */
div { width: 200px; padding: 20px; }  /* Actual: 240px wide */

/* border-box: width = content + padding + border */
div { width: 200px; padding: 20px; box-sizing: border-box; }  /* Actual: 200px wide */
```

### 3. CSS Gradients
**Concept:** Smooth color transitions as backgrounds.

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* 135deg = angle, two color stops with positions */
```

**Gradient types:**
```css
/* Linear — directional */
background: linear-gradient(to right, red, blue);
background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb);

/* Radial — circular/elliptical */
background: radial-gradient(circle, white, black);

/* Multiple color stops */
background: linear-gradient(90deg, red 0%, yellow 50%, green 100%);
```

### 4. Flexbox for Centering
**Concept:** Using flexbox to center content vertically and horizontally.

```css
body {
    display: flex;
    justify-content: center;  /* Horizontal center (main axis) */
    align-items: center;      /* Vertical center (cross axis) */
    min-height: 100vh;        /* Full viewport height */
}
```

**Flexbox cheat sheet:**
```css
.container {
    display: flex;
    flex-direction: row;       /* row | column | row-reverse | column-reverse */
    justify-content: center;   /* Main axis: flex-start|center|flex-end|space-between|space-around */
    align-items: center;       /* Cross axis: flex-start|center|flex-end|stretch|baseline */
    gap: 10px;                 /* Space between flex items */
    flex-wrap: wrap;           /* Allow items to wrap to next line */
}
```

**`vh` and `vw` units:**
```css
min-height: 100vh;   /* 100% of viewport height */
width: 50vw;         /* 50% of viewport width */
/* 1vh = 1% of viewport height */
```

### 5. Responsive Images
**Concept:** Images that scale with their container.

```css
img {
    width: 100%;
    height: 250px;
    object-fit: cover;   /* Crop to fill, maintain aspect ratio */
}
```

| `object-fit` | Behavior |
|-------------|----------|
| `cover` | Fill container, crop excess |
| `contain` | Fit inside, may have empty space |
| `fill` | Stretch to fill (may distort) |
| `none` | No resizing (original size) |
| `scale-down` | Smaller of `none` or `contain` |

### 6. CSS Transitions for Interactivity
**Concept:** Smooth animations on state changes (hover, focus).

```css
.rsvp-btn {
    transition: transform 0.2s, box-shadow 0.2s;
}
.rsvp-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}
```

**Transition syntax:**
```css
transition: property duration timing-function delay;
transition: all 0.3s ease;              /* All properties */
transition: transform 0.2s ease-in-out; /* Specific property */

/* Timing functions: ease | linear | ease-in | ease-out | ease-in-out */
```

**Common hover effects:**
```css
/* Lift effect */
:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }

/* Scale effect */
:hover { transform: scale(1.05); }

/* Color change */
:hover { background-color: #5a6fd6; }
```

### 7. Accessibility (a11y)
**Concept:** Making the page usable for screen readers and assistive tech.

```html
<img alt="Descriptive text for the image">
<a aria-label="RSVP via email" href="mailto:...">
<a target="_blank" rel="noopener noreferrer">  <!-- Security for new tab -->
```

**Key accessibility practices:**
- Every `<img>` needs an `alt` attribute (empty `alt=""` for decorative images)
- Use semantic elements (`<nav>`, `<main>`) instead of `<div>` with roles
- Ensure sufficient color contrast (4.5:1 ratio minimum)
- Links should describe their destination, not just "click here"

**`rel="noopener noreferrer"` explained:**
```html
<a target="_blank" rel="noopener noreferrer" href="...">
<!-- noopener: prevents new page from accessing window.opener (security) -->
<!-- noreferrer: prevents sending Referer header (privacy) -->
```

### 8. Viewport Meta Tag
**Concept:** Enabling responsive design on mobile devices.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

- Without this, mobile browsers render at ~980px width and zoom out
- `width=device-width` — layout width matches device screen width
- `initial-scale=1.0` — no zoom on page load

---

## Simple vs Production Comparison

| Aspect | Simple | Production |
|--------|--------|------------|
| **Styling** | No CSS | Full inline CSS with gradients |
| **Layout** | Default flow | Flexbox centered card layout |
| **Responsiveness** | Not responsive | Viewport meta + max-width + flexible images |
| **Accessibility** | Basic alt text | ARIA labels, semantic elements |
| **Interactivity** | Static links | Hover effects, transitions |
| **Visual design** | Plain HTML | Gradient backgrounds, shadows, rounded corners |
| **Security** | Basic links | `rel="noopener noreferrer"` on external links |
| **Box model** | Default content-box | `border-box` for predictable sizing |

### Why Production is Better
- **Professional appearance:** Gradient backgrounds, shadows, and typography
- **Mobile-friendly:** Responsive layout works on all screen sizes
- **Accessible:** Screen readers can navigate with semantic elements
- **Interactive:** Hover effects provide visual feedback
- **Secure:** External links use `noopener noreferrer`
- **Predictable sizing:** `border-box` prevents layout math surprises

# Flask Auth End - Application Analysis

## 1. Function Call Flow

### Entry Points
- **main.py line 125-126**: `if __name__ == "__main__": app.run(debug=True)` - Application startup

### Route Handlers
```
app.run(debug=True)
├── @app.route('/') → home() (line 44-46)
│   └── render_template("index.html", logged_in=current_user.is_authenticated)
│
├── @app.route('/register', methods=["GET", "POST"]) → register() (line 49-78)
│   ├── if request.method == "POST": (line 51)
│   │   ├── email = request.form.get('email') (line 53)
│   │   ├── db.session.execute(db.select(User).where(User.email == email)) (line 54)
│   │   ├── user = result.scalar() (line 57)
│   │   ├── if user: (line 58)
│   │   │   ├── flash("You've already signed up...") (line 60)
│   │   │   └── return redirect(url_for('login')) (line 61)
│   │   ├── hash_and_salted_password = generate_password_hash() (line 63-67)
│   │   ├── new_user = User(...) (line 68-72)
│   │   ├── db.session.add(new_user) (line 73)
│   │   ├── db.session.commit() (line 74)
│   │   ├── login_user(new_user) (line 75)
│   │   └── return redirect(url_for("secrets")) (line 76)
│   └── return render_template("register.html", logged_in=current_user.is_authenticated) (line 78)
│
├── @app.route('/login', methods=["GET", "POST"]) → login() (line 81-100)
│   ├── if request.method == "POST": (line 83)
│   │   ├── email = request.form.get('email') (line 84)
│   │   ├── password = request.form.get('password') (line 85)
│   │   ├── db.session.execute(db.select(User).where(User.email == email)) (line 87)
│   │   ├── user = result.scalar() (line 88)
│   │   ├── if not user: (line 90)
│   │   │   ├── flash("That email does not exist...") (line 91)
│   │   │   └── return redirect(url_for('login')) (line 92)
│   │   ├── elif not check_password_hash(user.password, password): (line 93)
│   │   │   ├── flash('Password incorrect...') (line 94)
│   │   │   └── return redirect(url_for('login')) (line 95)
│   │   ├── else: (line 96)
│   │   │   ├── login_user(user) (line 97)
│   │   │   └── return redirect(url_for('secrets')) (line 98)
│   └── return render_template("login.html", logged_in=current_user.is_authenticated) (line 100)
│
├── @app.route('/secrets') → secrets() (line 103-107)
│   ├── @login_required decorator (line 104)
│   ├── print(current_user.name) (line 106)
│   └── render_template("secrets.html", name=current_user.name, logged_in=True) (line 107)
│
├── @app.route('/logout') → logout() (line 110-114)
│   ├── @login_required decorator (line 111)
│   ├── logout_user() (line 113)
│   └── return redirect(url_for('home')) (line 114)
│
└── @app.route('/download') → download() (line 117-122)
    ├── @login_required decorator (line 118)
    └── send_from_directory('static', path="files/cheat_sheet.pdf") (line 122)
```

### Initialization Flow (lines 1-42)
```
Import statements (lines 1-6)
├── Flask: render_template, request, url_for, redirect, flash, send_from_directory
├── werkzeug.security: generate_password_hash, check_password_hash
├── flask_sqlalchemy.SQLAlchemy
├── sqlalchemy.orm: DeclarativeBase, Mapped, mapped_column
├── sqlalchemy: Integer, String
└── flask_login: UserMixin, login_user, LoginManager, login_required, current_user, logout_user

Flask App Configuration (lines 9-10)
├── app = Flask(__name__) (line 9)
└── app.config['SECRET_KEY'] = 'secret-key-goes-here' (line 10)

Database Configuration (lines 19-29)
├── class Base(DeclarativeBase) (lines 15-16)
├── app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' (line 19)
├── db = SQLAlchemy(model_class=Base) (line 20)
├── db.init_app(app) (line 21)
├── login_manager = LoginManager() (line 23)
├── login_manager.init_app(app) (line 24)
├── @login_manager.user_loader → load_user(user_id) (lines 27-29)
│   └── return db.get_or_404(User, user_id) (line 29)

Database Model (lines 33-37)
├── class User(UserMixin, db.Model) (line 33)
│   ├── id: Mapped[int] (primary key) (line 34)
│   ├── email: Mapped[str] (unique) (line 35)
│   ├── password: Mapped[str] (line 36)
│   └── name: Mapped[str] (line 37)
└── with app.app_context(): db.create_all() (lines 40-41)
```

### Decorators and Middleware
- **@login_manager.user_loader** (line 27): User loader callback for Flask-Login
- **@login_required** (lines 104, 111, 118): Route protection decorator - requires authentication

### Database Model

#### User Model (lines 33-37)
```
User.__init__() (implicit via SQLAlchemy)
├── id: Mapped[int] (primary key)
├── email: Mapped[str] (unique)
├── password: Mapped[str] (hashed)
└── name: Mapped[str]
```

---

## 2. Template Rendering Flow

### Template Loading Structure
```
Flask render_template() calls
├── home() → index.html (line 46)
│   ├── Context: logged_in=current_user.is_authenticated
│   ├── Extends: base.html (line 1)
│   └── Block: content
│
├── register() → register.html (line 78)
│   ├── Context: logged_in=current_user.is_authenticated
│   ├── Extends: base.html (line 1)
│   └── Block: content
│
├── login() → login.html (line 100)
│   ├── Context: logged_in=current_user.is_authenticated
│   ├── Extends: base.html (line 1)
│   └── Block: content
│
├── secrets() → secrets.html (line 107)
│   ├── Context: name=current_user.name, logged_in=True
│   ├── Extends: base.html (line 1)
│   └── Block: content
│
└── logout() → redirect (no template)
```

### Template: base.html
- **Extended by**: All templates (index.html, register.html, login.html, secrets.html)
- **Template location**: `templates/base.html`
- **Purpose**: Provides HTML head, navigation, and body structure
- **CSS references**:
  - Bootstrap 4.5.2 from CDN (line 10)
  - Custom styles.css (line 14)
- **Navigation logic** (lines 27-34):
  - Shows Login/Register links if `not logged_in`
  - Always shows Log Out link

### Template: index.html
- **Rendered by**: `home()` at main.py line 46
- **Context variables passed**: `logged_in` (boolean)
- **Template location**: `templates/index.html`
- **Extends**: base.html (line 1)
- **Conditional display**:
  - Shows Login/Register buttons if not logged in (lines 8-16)
  - Shows feedback message if logged in (lines 18-20)

### Template: register.html
- **Rendered by**: `register()` at main.py line 78
- **Context variables passed**: `logged_in` (boolean)
- **Template location**: `templates/register.html`
- **Extends**: base.html (line 1)
- **Form action**: `{{ url_for('register') }}` (line 6)
- **Form method**: POST (line 6)
- **Form fields**: name, email, password

### Template: login.html
- **Rendered by**: `login()` at main.py line 100
- **Context variables passed**: `logged_in` (boolean)
- **Template location**: `templates/login.html`
- **Extends**: base.html (line 1)
- **Form method**: POST (line 14)
- **Flash messages**: Displays login errors (lines 7-13)
- **Form fields**: email, password

### Template: secrets.html
- **Rendered by**: `secrets()` at main.py line 107
- **Context variables passed**: `name` (string), `logged_in=True`
- **Template location**: `templates/secrets.html`
- **Extends**: base.html (line 1)
- **Protected by**: @login_required decorator
- **Download link**: Points to `/download` route (line 6)

### Template Inheritance
- **Template inheritance using {% extends %}** - All templates extend base.html
- **Base template**: base.html provides structure
- **Blocks**: All templates use `{% block content %}` block
- **Navigation**: Shared navigation in base.html with conditional logic

### Context Data Flow
```
Python → Template Context
├── main.py line 46: logged_in=current_user.is_authenticated → index.html
│   └── logged_in (boolean) → {% if not logged_in: %}
│
├── main.py line 78: logged_in=current_user.is_authenticated → register.html
│   └── logged_in (boolean) → {% if not logged_in: %} in base.html
│
├── main.py line 100: logged_in=current_user.is_authenticated → login.html
│   └── logged_in (boolean) → {% if not logged_in: %} in base.html
│
└── main.py line 107: name=current_user.name, logged_in=True → secrets.html
    ├── name (string) → {{name}}
    └── logged_in (boolean) → {% if not logged_in: %} in base.html
```

---

## 3. Template Loop Analysis

### login.html Loop (lines 9-11)
```jinja2
{% for message in messages %}
    <p>{{ message }}</p>
{% endfor %}
```

**Loop Details:**
- **Data source**: `messages` (list of flash messages)
- **Provided by**: `get_flashed_messages()` at line 7
- **Iteration variable**: `message` (individual flash message string)
- **Variables available inside loop**:
  - `message` - Flash message text
- **HTML elements rendered per iteration**:
  - `<p>{{ message }}</p>` - Flash message paragraph

### index.html
- **No loops present** - Conditional display only

### register.html
- **No loops present** - Form-based page

### secrets.html
- **No loops present** - Protected content page

### base.html
- **No loops present** - Navigation and structure

---

## 4. Static File References

### CSS File References

#### base.html (line 10)
```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" />
```
- **CSS file**: Bootstrap 4.5.2 from CDN
- **Purpose**: Bootstrap CSS framework

#### base.html (line 14)
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css')}}" />
```
- **CSS file**: `static/css/styles.css`
- **Path reference**: Flask url_for helper
- **Purpose**: Custom styling for authentication pages

### JavaScript File References
- **None** - No JavaScript files referenced

### CSS Classes Used (Bootstrap + Custom)

#### Bootstrap Classes
**Navigation:**
- `.navbar` - Navbar container
- `.navbar-expand-lg` - Responsive navbar
- `.navbar-light` - Light theme
- `.bg-light` - Light background
- `.navbar-brand` - Brand/logo
- `.navbar-collapse` - Collapsible content
- `.navbar-nav` - Navigation links
- `.nav-item` - Navigation item
- `.nav-link` - Navigation link
- `.ml-auto` - Margin left auto

**Components:**
- `.btn` - Button base
- `.btn-primary` - Primary button
- `.btn-secondary` - Secondary button
- `.btn-block` - Full-width button
- `.btn-large` - Large button
- `.container` - Container for content

#### Custom Classes (styles.css)
**Layout:**
- `.box` - Centered box container (lines 38-45)
- `.container` - Content container (lines 47-50, 53-56)

**Typography:**
- `.title` - Title styling (used in secrets.html)

**Buttons:**
- `.btn` - Custom button styling (lines 2-10)
- `.btn-large` - Large button variant (line 4)
- `.btn-primary` - Primary button variant (lines 6-9)
- `.btn-block` - Block button (line 10)

**Inputs:**
- `input` - Form input styling (lines 60-79)

### External Resources

#### Bootstrap 4.5.2 (base.html line 10)
```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" />
```
- **Purpose**: Bootstrap CSS framework
- **CDN**:stackpath.bootstrapcdn.com

#### Google Fonts (styles.css line 1)
```css
@import url(https://fonts.googleapis.com/css?family=Open+Sans);
```
- **Purpose**: Load Open Sans font family
- **Applied to**: Body text via CSS (line 19)

### File Download Reference

#### secrets.html (line 6)
```html
<a href="{{ url_for('download') }}">Download Your File</a>
```
- **Route**: `/download`
- **File**: `static/files/cheat_sheet.pdf`
- **Purpose**: Download protected file for authenticated users

### Image/Asset References
- **None** - No images referenced in templates

---

## 5. Data Flow Diagram

```mermaid
graph TD
    A[User Request] --> B{Route Matching}
    B -->|/| C[home]
    B -->|/register GET/POST| D[register]
    B -->|/login GET/POST| E[login]
    B -->|/secrets| F[secrets]
    B -->|/logout| G[logout]
    B -->|/download| H[download]
    
    C --> I[render_template index.html]
    D --> J[render_template register.html]
    E --> K[render_template login.html]
    F --> L[render_template secrets.html]
    G --> M[redirect home]
    H --> N[send_from_directory]
    
    I --> O[HTML Response]
    J --> O
    K --> O
    L --> O
    M --> C
    N --> P[PDF File Download]
    
    D --> Q{POST Request?}
    Q -->|Yes| R[validate form]
    Q -->|No| J
    R --> S{Email exists?}
    S -->|Yes| T[flash error]
    S -->|No| U[hash password]
    T --> M
    U --> V[create User]
    V --> W[db.session.add]
    W --> X[db.session.commit]
    X --> Y[login_user]
    Y --> F
    
    E --> Z{POST Request?}
    Z -->|Yes| AA[validate form]
    Z -->|No| K
    AA --> AB[check credentials]
    AB --> AC{Valid?}
    AC -->|No| AD[flash error]
    AC -->|Yes| AE[login_user]
    AD --> M
    AE --> F
    
    F --> AF{@login_required}
    AF --> AG{Authenticated?}
    AG -->|No| AH[redirect login]
    AG -->|Yes| L
    
    G --> AF
    AF --> AI[logout_user]
    AI --> M
    
    H --> AF
    AF --> N
    
    BB[SQLite Database users.db] --> BC[User table]
    
    BC --> D
    BC --> E
    BC --> F
    
    CC[static/css/styles.css] --> CD[CSS Styling]
    CD --> O
    
    CE[Bootstrap CDN] --> CF[Bootstrap Styles]
    CF --> O
    
    style C fill:#e1f5ff
    style D fill:#e1f5ff
    style E fill:#e1f5ff
    style F fill:#e1f5ff
    style G fill:#e1f5ff
    style H fill:#e1f5ff
    style I fill:#fff4e1
    style J fill:#fff4e1
    style K fill:#fff4e1
    style L fill:#fff4e1
    style M fill:#fff4e1
    style N fill:#fff4e1
    style O fill:#e8f5e9
    style P fill:#e8f5e9
```

### ASCII Art Data Flow
```
┌─────────────────────────────────────────────────────────────────┐
│                        USER REQUEST                              │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   Flask Router        │
              └───────────┬───────────┘
                          │
    ┌─────────────────────┼─────────────────────┬──────────────┐
    │                     │                     │              │
    ▼                     ▼                     ▼              ▼
┌─────────┐         ┌─────────┐         ┌──────────────┐  ┌──────────┐
│ Route:  │         │ Route:  │         │ Route:       │  │ Route:   │
│   /     │         │/register│         │ /login       │  │/secrets  │
│ home()  │         │register()│         │ login()      │  │secrets() │
└────┬────┘         └────┬────┘         └──────┬───────┘  └────┬─────┘
     │                   │                     │               │
     │                   │                     │               │
     │                   ▼                     ▼               │
     │            ┌──────────────┐     ┌──────────────┐        │
     │            │ POST?        │     │ POST?        │        │
     │            └──────┬───────┘     └──────┬───────┘        │
     │              Yes │              Yes │                 │
     │                   ▼                   ▼                 │
     │            ┌──────────────┐   ┌──────────────┐         │
     │            │check email   │   │check email   │         │
     │            │exists?       │   │& password    │         │
     │            └──────┬───────┘   └──────┬───────┘         │
     │                   │                   │                 │
     │            ┌──────┴───────┐   ┌──────┴───────┐         │
     │            │              │   │              │         │
     │            ▼              ▼   ▼              ▼         │
     │       ┌─────────┐  ┌─────────┐  ┌─────────┐          │
     │       │hash pwd │  │flash err│  │login_user│          │
     │       │create   │  │redirect │  │redirect │          │
     │       │User     │  │to login │  │to secrets│          │
     │       └────┬────┘  └─────────┘  └─────────┘          │
     │            │                                              │
     │            ▼                                              │
     │       ┌─────────┐                                         │
     │       │save to  │                                         │
     │       │DB       │                                         │
     │       └────┬────┘                                         │
     │            │                                              │
     │            ▼                                              │
     │       ┌─────────┐                                         │
     │       │login_user│                                         │
     │       └────┬────┘                                         │
     │            │                                              │
     └────────────┴─────────────┬───────────────────┐           │
                              │                   │           │
                              ▼                   ▼           │
                    ┌──────────────────┐  ┌──────────────┐    │
                    │render_template   │  │@login_required│    │
                    │index.html        │  │check          │    │
                    │logged_in=        │  │authenticated? │    │
                    │current_user.     │  └──────┬───────┘    │
                    │is_authenticated │         │             │
                    └────────┬─────────┘         │             │
                             │              ┌────┴────┐         │
                             │              │         │         │
                             ▼              ▼         ▼         │
                    ┌──────────────────┐  ┌─────┐  ┌─────┐   │
                    │Extend base.html  │  │Yes │  │No  │   │
                    │Conditional nav   │  └──┬──┘  └──┬──┘   │
                    │Login/Register    │     │        │       │
                    │buttons           │     │        │       │
                    └────────┬─────────┘     │        │       │
                             │              │        │       │
                             │              │        │       │
                             ▼              │        │       │
                    ┌──────────────────┐     │        │       │
                    │  HTML Response   │     │        │       │
                    │  + CSS Styling   │     │        │       │
                    └────────┬─────────┘     │        │       │
                             │              │        │       │
                             │              │        │       │
                             └──────────────┼────────┘       │
                                            │                │
                                            ▼                │
                                    ┌──────────────┐         │
                                    │render_template │         │
                                    │secrets.html    │         │
                                    │name=current_user│        │
                                    │.name           │         │
                                    └──────┬───────┘         │
                                           │                │
                                           ▼                │
                                    ┌──────────────┐         │
                                    │Download link  │         │
                                    │to /download   │         │
                                    └──────┬───────┘         │
                                           │                │
                                           ▼                │
                                    ┌──────────────┐         │
                                    │send_from_     │         │
                                    │directory      │         │
                                    │cheat_sheet.pdf│         │
                                    └──────┬───────┘         │
                                           │                │
                                           ▼                │
                                    ┌──────────────┐         │
                                    │PDF File      │         │
                                    │Download      │         │
                                    └──────────────┘         │
                                                            │
                                                            ▼
                                                    ┌──────────────┐
                                                    │redirect login│
                                                    └──────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    AUTHENTICATION FLOW                           │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐
│  Register    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Form Data   │
│  email, pwd  │
│  name        │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Check email │
│  exists in   │
│  DB?         │
└──────┬───────┘
       │
       ├────Yes──┐
       │         ▼
       │    ┌──────────────┐
       │    │Flash error   │
       │    │Redirect login│
       │    └──────────────┘
       │
       ▼
┌──────────────┐
│  Hash pwd    │
│  pbkdf2:sha256│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Create User │
│  object      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Save to DB  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  login_user()│
│  (Flask-Login)│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Redirect    │
│  to secrets  │
└──────────────┘

┌──────────────┐
│  Login       │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Form Data   │
│  email, pwd  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Find user   │
│  by email    │
└──────┬───────┘
       │
       ├────No───┐
       │         ▼
       │    ┌──────────────┐
       │    │Flash error   │
       │    │Redirect login│
       │    └──────────────┘
       │
       ▼
┌──────────────┐
│  Check pwd   │
│  hash        │
└──────┬───────┘
       │
       ├────Invalid─┐
       │            ▼
       │     ┌──────────────┐
       │     │Flash error   │
       │     │Redirect login│
       │     └──────────────┘
       │
       ▼
┌──────────────┐
│  login_user()│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Redirect    │
│  to secrets  │
└──────────────┘

┌──────────────┐
│  Logout      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  logout_user()│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Redirect    │
│  to home     │
└──────────────┘
```

---

## 6. Written Summary

### Application Architecture
This is a **Flask authentication application** demonstrating user registration, login, and protected routes. It follows a **simple MVC pattern**:
- **Model**: SQLAlchemy ORM model (User) for database representation
- **View**: HTML templates with Jinja2 template inheritance
- **Controller**: Flask routes handling authentication logic and protected resources

### Request Lifecycle Walkthrough

#### 1. Application Startup
1. Python executes `main.py`
2. Imports Flask, SQLAlchemy, Flask-Login, and dependencies (lines 1-6)
3. Initializes Flask application with SECRET_KEY (lines 9-10)
4. Configures SQLite database (line 19)
5. Configures Flask-Login for authentication (lines 23-29)
6. Defines User model with id, email, password, name (lines 33-37)
7. Creates database tables if they don't exist (lines 40-41)
8. Starts development server with debug mode (line 126)

#### 2. Homepage Request (`/`)
1. User navigates to `http://localhost:5000/`
2. Flask router matches route to `home()` function
3. Function renders `index.html` with `logged_in=current_user.is_authenticated` context
4. Template extends `base.html`
5. Base template includes navigation with conditional logic
6. Index template shows Login/Register buttons if not logged in
7. Shows feedback message if already logged in
8. Bootstrap CSS and custom styles applied
9. HTML response returned to browser

#### 3. Registration Request (`/register`)
1. User clicks "Register" link in navigation
2. Flask router matches route to `register()` function
3. **GET request**: Renders `register.html` with `logged_in` context
4. Template extends `base.html`
5. Registration form displayed with name, email, password fields
6. **POST request** (form submission):
   - Extracts email from form data (line 53)
   - Checks if email already exists in database (line 54-57)
   - If exists: flashes error and redirects to login (line 60-61)
   - If new: hashes password using pbkdf2:sha256 (line 63-67)
   - Creates new User object (line 68-72)
   - Saves to database (line 73-74)
   - Authenticates user with Flask-Login (line 75)
   - Redirects to secrets page (line 76)
7. HTML response returned to browser

#### 4. Login Request (`/login`)
1. User clicks "Login" link in navigation
2. Flask router matches route to `login()` function
3. **GET request**: Renders `login.html` with `logged_in` context
4. Template extends `base.html`
5. Login form displayed with email, password fields
6. **POST request** (form submission):
   - Extracts email and password from form data (lines 84-85)
   - Queries database for user by email (line 87-88)
   - If email doesn't exist: flashes error and redirects to login (line 91-92)
   - If password incorrect: flashes error and redirects to login (line 94-95)
   - If credentials valid: authenticates user with Flask-Login (line 97)
   - Redirects to secrets page (line 98)
7. Flash messages displayed for errors (lines 7-13 in template)
8. HTML response returned to browser

#### 5. Secrets Page Request (`/secrets`)
1. User navigates to `/secrets` (after login)
2. Flask router matches route to `secrets()` function
3. **@login_required decorator** checks if user is authenticated (line 104)
4. If not authenticated: redirects to login page
5. If authenticated:
   - Prints current user name to console (line 106)
   - Renders `secrets.html` with `name=current_user.name` and `logged_in=True` context (line 107)
6. Template extends `base.html`
7. Template displays welcome message with user name
8. Template provides download link for protected file
9. HTML response returned to browser

#### 6. Logout Request (`/logout`)
1. User clicks "Log Out" link in navigation
2. Flask router matches route to `logout()` function
3. **@login_required decorator** checks if user is authenticated (line 111)
4. If not authenticated: redirects to login page
5. If authenticated:
   - Calls `logout_user()` from Flask-Login (line 113)
   - Redirects to homepage (line 114)
6. Navigation now shows Login/Register links instead of Logout

#### 7. Download Request (`/download`)
1. User clicks "Download Your File" link on secrets page
2. Flask router matches route to `download()` function
3. **@login_required decorator** checks if user is authenticated (line 118)
4. If not authenticated: redirects to login page
5. If authenticated:
   - Serves file from static directory (line 122)
   - File: `static/files/cheat_sheet.pdf`
6. PDF file downloaded to user's computer

### Key Files and Responsibilities

#### main.py (3679 bytes)
- **Lines 1-6**: Import statements
- **Lines 9-10**: Flask app initialization
- **Lines 15-29**: Database and Flask-Login configuration
- **Lines 33-37**: User model definition
- **Lines 40-41**: Database table creation
- **Lines 44-46**: Homepage route
- **Lines 49-78**: Registration route
- **Lines 81-100**: Login route
- **Lines 103-107**: Secrets page route (protected)
- **Lines 110-114**: Logout route (protected)
- **Lines 117-122**: Download route (protected)
- **Lines 125-126**: Application startup

#### requirements.txt (94 bytes)
- **Flask_Login==0.6.3**: User authentication
- **Werkzeug==3.0.0**: Password hashing
- **Flask==3.0.0**: Web framework
- **flask_sqlalchemy==3.1.1**: ORM
- **SQLAlchemy==2.0.25**: Database toolkit

#### templates/base.html (1418 bytes)
- **Lines 1-16**: HTML head with Bootstrap and custom CSS
- **Lines 18-40**: Navigation bar with conditional logic
- **Lines 41-42**: Content block
- **Purpose**: Base template with navigation

#### templates/index.html (531 bytes)
- **Line 1**: Extends base.html
- **Lines 4-20**: Content with conditional Login/Register buttons
- **Purpose**: Homepage with authentication status

#### templates/register.html (522 bytes)
- **Line 1**: Extends base.html
- **Lines 4-12**: Registration form
- **Purpose**: User registration page

#### templates/login.html (663 bytes)
- **Line 1**: Extends base.html
- **Lines 4-19**: Login form with flash messages
- **Purpose**: User login page

#### templates/secrets.html (200 bytes)
- **Line 1**: Extends base.html
- **Lines 4-7**: Protected content with download link
- **Purpose**: Protected page for authenticated users

#### static/css/styles.css (5991 bytes)
- **Line 1**: Google Fonts import
- **Lines 2-10**: Button styling
- **Lines 12-27**: Body gradient background
- **Lines 29-36**: Link and paragraph styling
- **Lines 38-45**: Box container styling
- **Lines 47-56**: Container styling
- **Lines 60-79**: Input field styling
- **Purpose**: Custom styling for authentication pages

#### static/files/cheat_sheet.pdf (65007 bytes)
- **Purpose**: Protected file download for authenticated users

### Configuration
- **Debug mode**: Enabled (`debug=True`)
- **Host**: Default (127.0.0.1)
- **Port**: Default (5000)
- **Template folder**: `templates/` (Flask default)
- **Static folder**: `static/` (Flask default)
- **Database**: SQLite (`sqlite:///users.db`)
- **SECRET_KEY**: 'secret-key-goes-here' (placeholder)

### Database
- **Type**: SQLite
- **Location**: `instance/users.db`
- **ORM**: SQLAlchemy 2.0.25
- **Table**: `users`
- **Fields**:
  - id: Integer (primary key)
  - email: String(100, unique)
  - password: String(100, hashed)
  - name: String(1000)
- **Data persistence**: Persistent (SQLite file)

### Security Considerations
- Password hashing using pbkdf2:sha256 with salt (lines 63-67)
- User authentication via Flask-Login
- Route protection using @login_required decorator
- CSRF protection via Flask (SECRET_KEY)
- Input validation via HTML5 required attributes
- SQL injection protection via SQLAlchemy ORM
- No HTTPS enforcement
- Debug mode enabled (not production-ready)
- SECRET_KEY is placeholder (needs to be changed for production)
- No rate limiting on login attempts

### Technology Stack
- **Framework**: Flask 3.0.0 (Python web framework)
- **ORM**: SQLAlchemy 2.0.25 with Flask-SQLAlchemy
- **Authentication**: Flask-Login 0.6.3
- **Password Security**: Werkzeug 3.0.0
- **CSS Framework**: Bootstrap 4.5.2
- **Templating**: Jinja2 (Flask's default)
- **Database**: SQLite

### External Dependencies
- **Bootstrap 4.5.2**: CSS framework (loaded from CDN)
- **Google Fonts**: Open Sans font family (loaded from fonts.googleapis.com)

### Protected Resources
- **/secrets**: Protected page requiring authentication
- **/logout**: Protected route requiring authentication
- **/download**: Protected file download requiring authentication
- **File**: `static/files/cheat_sheet.pdf` - Only accessible to authenticated users

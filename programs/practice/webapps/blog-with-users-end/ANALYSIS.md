# Blog with Users End - Application Analysis

## 1. Function Call Flow

### Entry Points
- **main.py line 276-277**: `if __name__ == "__main__": app.run(debug=True, port=5001)` - Application startup

### Route Handlers
```
app.run(debug=True, port=5001)
├── @app.route('/') → get_all_posts() (line 185-189)
│   ├── db.session.execute(db.select(BlogPost)) (line 187)
│   ├── posts = result.scalars().all() (line 188)
│   └── render_template("index.html", all_posts=posts, current_user=current_user) (line 189)
│
├── @app.route('/register', methods=["GET", "POST"]) → register() (line 125-153)
│   ├── form = RegisterForm() (line 127)
│   ├── if form.validate_on_submit(): (line 128)
│   │   ├── db.session.execute(db.select(User).where(User.email == form.email.data)) (line 131)
│   │   ├── user = result.scalar() (line 132)
│   │   ├── if user: (line 133)
│   │   │   ├── flash("You've already signed up...") (line 135)
│   │   │   └── return redirect(url_for('login')) (line 136)
│   │   ├── hash_and_salted_password = generate_password_hash() (line 138-142)
│   │   ├── new_user = User(...) (line 143-147)
│   │   ├── db.session.add(new_user) (line 148)
│   │   ├── db.session.commit() (line 149)
│   │   ├── login_user(new_user) (line 151)
│   │   └── return redirect(url_for("get_all_posts")) (line 152)
│   └── render_template("register.html", form=form, current_user=current_user) (line 153)
│
├── @app.route('/login', methods=["GET", "POST"]) → login() (line 156-176)
│   ├── form = LoginForm() (line 158)
│   ├── if form.validate_on_submit(): (line 159)
│   │   ├── password = form.password.data (line 160)
│   │   ├── db.session.execute(db.select(User).where(User.email == form.email.data)) (line 161)
│   │   ├── user = result.scalar() (line 163)
│   │   ├── if not user: (line 165)
│   │   │   ├── flash("That email does not exist...") (line 166)
│   │   │   └── return redirect(url_for('login')) (line 167)
│   │   ├── elif not check_password_hash(user.password, password): (line 169)
│   │   │   ├── flash('Password incorrect...') (line 170)
│   │   │   └── return redirect(url_for('login')) (line 171)
│   │   ├── else: (line 172)
│   │   │   ├── login_user(user) (line 173)
│   │   │   └── return redirect(url_for('get_all_posts')) (line 174)
│   └── render_template("login.html", form=form, current_user=current_user) (line 176)
│
├── @app.route('/logout') → logout() (line 179-182)
│   ├── logout_user() (line 181)
│   └── return redirect(url_for('get_all_posts')) (line 182)
│
├── @app.route("/post/<int:post_id>", methods=["GET", "POST"]) → show_post(post_id) (line 193-211)
│   ├── requested_post = db.get_or_404(BlogPost, post_id) (line 195)
│   ├── comment_form = CommentForm() (line 197)
│   ├── if comment_form.validate_on_submit(): (line 199)
│   │   ├── if not current_user.is_authenticated: (line 200)
│   │   │   ├── flash("You need to login...") (line 201)
│   │   │   └── return redirect(url_for("login")) (line 202)
│   │   ├── new_comment = Comment(...) (line 204-208)
│   │   ├── db.session.add(new_comment) (line 209)
│   │   └── db.session.commit() (line 210)
│   └── render_template("post.html", post=requested_post, current_user=current_user, form=comment_form) (line 211)
│
├── @app.route("/new-post", methods=["GET", "POST"]) → add_new_post() (line 215-231)
│   ├── @admin_only decorator (line 216)
│   ├── form = CreatePostForm() (line 218)
│   ├── if form.validate_on_submit(): (line 219)
│   │   ├── new_post = BlogPost(...) (line 220-227)
│   │   ├── db.session.add(new_post) (line 228)
│   │   ├── db.session.commit() (line 229)
│   │   └── return redirect(url_for("get_all_posts")) (line 230)
│   └── render_template("make-post.html", form=form, current_user=current_user) (line 231)
│
├── @app.route("/edit-post/<int:post_id>", methods=["GET", "POST"]) → edit_post(post_id) (line 235-253)
│   ├── post = db.get_or_404(BlogPost, post_id) (line 237)
│   ├── edit_form = CreatePostForm(...) (line 238-244)
│   ├── if edit_form.validate_on_submit(): (line 245)
│   │   ├── post.title = edit_form.title.data (line 246)
│   │   ├── post.subtitle = edit_form.subtitle.data (line 247)
│   │   ├── post.img_url = edit_form.img_url.data (line 248)
│   │   ├── post.author = current_user (line 249)
│   │   ├── post.body = edit_form.body.data (line 250)
│   │   ├── db.session.commit() (line 251)
│   │   └── return redirect(url_for("show_post", post_id=post.id)) (line 252)
│   └── render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user) (line 253)
│
├── @app.route("/delete/<int:post_id>") → delete_post(post_id) (line 257-263)
│   ├── @admin_only decorator (line 258)
│   ├── post_to_delete = db.get_or_404(BlogPost, post_id) (line 260)
│   ├── db.session.delete(post_to_delete) (line 261)
│   ├── db.session.commit() (line 262)
│   └── return redirect(url_for('get_all_posts')) (line 263)
│
├── @app.route("/about") → about() (line 266-268)
│   └── render_template("about.html", current_user=current_user) (line 268)
│
└── @app.route("/contact") → contact() (line 271-273)
    └── render_template("contact.html", current_user=current_user) (line 273)
```

### Initialization Flow (lines 1-109)
```
Import statements (lines 1-14)
├── datetime.date
├── Flask components: abort, render_template, redirect, url_for, flash
├── flask_bootstrap.Bootstrap5
├── flask_ckeditor.CKEditor
├── flask_gravatar.Gravatar
├── flask_login components: UserMixin, login_user, LoginManager, current_user, logout_user
├── flask_sqlalchemy components: SQLAlchemy
├── sqlalchemy.orm components: relationship, DeclarativeBase, Mapped, mapped_column
├── sqlalchemy types: Integer, String, Text
├── functools.wraps
├── werkzeug.security: generate_password_hash, check_password_hash
└── forms: CreatePostForm, RegisterForm, LoginForm, CommentForm

Flask App Configuration (lines 29-32)
├── app = Flask(__name__) (line 29)
├── app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b' (line 30)
├── ckeditor = CKEditor(app) (line 31)
└── Bootstrap5(app) (line 32)

Flask-Login Configuration (lines 34-41)
├── login_manager = LoginManager() (line 35)
├── login_manager.init_app(app) (line 36)
└── @login_manager.user_loader → load_user(user_id) (lines 39-41)
    └── return db.get_or_404(User, user_id) (line 41)

Gravatar Configuration (lines 44-52)
├── gravatar = Gravatar(app, ...) (lines 45-52)
└── Parameters: size=100, rating='g', default='retro', etc.

Database Configuration (lines 54-109)
├── class Base(DeclarativeBase) (lines 55-56)
├── app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' (line 57)
├── db = SQLAlchemy(model_class=Base) (line 58)
├── db.init_app(app) (line 59)
├── class BlogPost(db.Model) (lines 63-76)
│   ├── id, author_id, title, subtitle, date, body, img_url
│   ├── author = relationship("User", back_populates="posts") (line 69)
│   └── comments = relationship("Comment", back_populates="parent_post") (line 76)
├── class User(UserMixin, db.Model) (lines 80-90)
│   ├── id, email, password, name
│   ├── posts = relationship("BlogPost", back_populates="author") (line 88)
│   └── comments = relationship("Comment", back_populates="comment_author") (line 90)
├── class Comment(db.Model) (lines 94-104)
│   ├── id, text, author_id, post_id
│   ├── comment_author = relationship("User", back_populates="comments") (line 101)
│   └── parent_post = relationship("BlogPost", back_populates="comments") (line 104)
└── with app.app_context(): db.create_all() (lines 107-108)
```

### Decorator Functions

#### admin_only Decorator (lines 112-121)
```
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function
```

### Database Models

#### BlogPost Model (lines 63-76)
```
BlogPost.__init__() (implicit via SQLAlchemy)
├── id: Mapped[int] (primary key)
├── author_id: Mapped[int] (foreign key to users.id)
├── author: relationship("User", back_populates="posts")
├── title: Mapped[str] (unique, nullable=False)
├── subtitle: Mapped[str] (nullable=False)
├── date: Mapped[str] (nullable=False)
├── body: Mapped[Text] (nullable=False)
├── img_url: Mapped[str] (nullable=False)
└── comments: relationship("Comment", back_populates="parent_post")
```

#### User Model (lines 80-90)
```
User.__init__() (implicit via SQLAlchemy)
├── id: Mapped[int] (primary key)
├── email: Mapped[str] (unique)
├── password: Mapped[str] (hashed)
├── name: Mapped[str]
├── posts: relationship("BlogPost", back_populates="author")
└── comments: relationship("Comment", back_populates="comment_author")
```

#### Comment Model (lines 94-104)
```
Comment.__init__() (implicit via SQLAlchemy)
├── id: Mapped[int] (primary key)
├── text: Mapped[Text] (nullable=False)
├── author_id: Mapped[int] (foreign key to users.id)
├── comment_author: relationship("User", back_populates="comments")
├── post_id: Mapped[int] (foreign key to blog_posts.id)
└── parent_post: relationship("BlogPost", back_populates="comments")
```

### Form Classes (forms.py)

#### CreatePostForm (lines 8-13)
```
CreatePostForm fields:
├── title: StringField(validators=[DataRequired()])
├── subtitle: StringField(validators=[DataRequired()])
├── img_url: StringField(validators=[DataRequired(), URL()])
├── body: CKEditorField(validators=[DataRequired()])
└── submit: SubmitField()
```

#### RegisterForm (lines 17-21)
```
RegisterForm fields:
├── email: StringField(validators=[DataRequired()])
├── password: PasswordField(validators=[DataRequired()])
├── name: StringField(validators=[DataRequired()])
└── submit: SubmitField()
```

#### LoginForm (lines 25-28)
```
LoginForm fields:
├── email: StringField(validators=[DataRequired()])
├── password: PasswordField(validators=[DataRequired()])
└── submit: SubmitField()
```

#### CommentForm (lines 32-34)
```
CommentForm fields:
├── comment_text: CKEditorField(validators=[DataRequired()])
└── submit: SubmitField()
```

---

## 2. Template Rendering Flow

### Template Loading Structure
```
Flask render_template() calls
├── get_all_posts() → index.html (line 189)
│   ├── Context: all_posts=posts, current_user=current_user
│   ├── Includes: header.html (line 1)
│   └── Includes: footer.html (line 65)
│
├── register() → register.html (line 153)
│   ├── Context: form=form, current_user=current_user
│   ├── Includes: header.html (line 2)
│   └── Includes: footer.html (line 32)
│
├── login() → login.html (line 176)
│   ├── Context: form=form, current_user=current_user
│   ├── Includes: header.html (line 3)
│   └── Includes: footer.html (line 42)
│
├── logout() → redirect (no template)
│
├── show_post(post_id) → post.html (line 211)
│   ├── Context: post=requested_post, current_user=current_user, form=comment_form
│   ├── Imports: render_form from bootstrap5/form.html (line 1)
│   ├── Includes: header.html (line 2)
│   └── Includes: footer.html (line 72)
│
├── add_new_post() → make-post.html (line 231)
│   ├── Context: form=form, current_user=current_user
│   ├── Imports: render_form from bootstrap5/form.html (line 1)
│   ├── Includes: header.html (line 3)
│   └── Includes: footer.html (line 39)
│
├── edit_post(post_id) → make-post.html (line 253)
│   ├── Context: form=edit_form, is_edit=True, current_user=current_user
│   ├── Imports: render_form from bootstrap5/form.html (line 1)
│   ├── Includes: header.html (line 3)
│   └── Includes: footer.html (line 39)
│
├── delete_post(post_id) → redirect (no template)
│
├── about() → about.html (line 268)
│   ├── Context: current_user=current_user
│   ├── Includes: header.html (line 1)
│   └── Includes: footer.html (line 47)
│
└── contact() → contact.html (line 273)
    ├── Context: current_user=current_user
    ├── Includes: header.html (line 1)
    └── Includes: footer.html (line 100)
```

### Template: header.html
- **Included by**: All templates (index.html, register.html, login.html, post.html, make-post.html, about.html, contact.html)
- **Template location**: `templates/header.html`
- **Purpose**: Provides HTML head, navigation, and body opening
- **CSS reference**: 
  - `{{ bootstrap.load_css() }}` (line 14) - Bootstrap-Flask CSS
  - `{{ url_for('static', filename='css/styles.css') }}` (line 38) - Custom CSS
- **External resources**:
  - Font Awesome icons (line 21-24)
  - Google Fonts - Lora and Open Sans (lines 26-35)
  - Favicon (line 16-19)
- **Navigation logic** (lines 69-93):
  - Shows Login/Register links if user is NOT authenticated
  - Shows Logout link if user IS authenticated

### Template: footer.html
- **Included by**: All templates (index.html, register.html, login.html, post.html, make-post.html, about.html, contact.html)
- **Template location**: `templates/footer.html`
- **Purpose**: Provides footer content, scripts, and body closing
- **JavaScript references**:
  - Bootstrap core JS from CDN (line 38)
  - Custom scripts.js (line 40)

### Template: index.html
- **Rendered by**: `get_all_posts()` at main.py line 189
- **Context variables passed**: `all_posts` (list of BlogPost objects), `current_user`
- **Template location**: `templates/index.html`
- **Includes**: header.html (line 1), footer.html (line 65)
- **Background image**: `../static/assets/img/home-bg.jpg` (line 6)
- **Admin-only features**:
  - Delete button for posts (lines 36-38)
  - Create New Post button (lines 47-55)

### Template: post.html
- **Rendered by**: `show_post(post_id)` at main.py line 211
- **Context variables passed**: `post` (BlogPost object), `current_user`, `form` (CommentForm)
- **Template location**: `templates/post.html`
- **Imports**: `render_form` from bootstrap5/form.html (line 1)
- **Includes**: header.html (line 2), footer.html (line 72)
- **Background image**: `{{post.img_url}}` (line 5)
- **CKEditor integration**: Loaded and configured (lines 43-45)
- **Admin-only feature**: Edit Post button (lines 31-39)
- **Comments section**: Displays all comments with Gravatar images (lines 48-64)

### Template: register.html
- **Rendered by**: `register()` at main.py line 153
- **Context variables passed**: `form` (RegisterForm), `current_user`
- **Template location**: `templates/register.html`
- **Imports**: `render_form` from bootstrap5/form.html (line 1)
- **Includes**: header.html (line 2), footer.html (line 32)
- **Background image**: `../static/assets/img/register-bg.jpg` (line 7)
- **Block**: Uses `{% block content %}` (line 1)

### Template: login.html
- **Rendered by**: `login()` at main.py line 176
- **Context variables passed**: `form` (LoginForm), `current_user`
- **Template location**: `templates/login.html`
- **Imports**: `render_form` from bootstrap5/form.html (line 1)
- **Includes**: header.html (line 3), footer.html (line 42)
- **Background image**: `../static/assets/img/login-bg.jpg` (line 8)
- **Flash messages**: Displays login errors (lines 26-32)
- **Block**: Uses `{% block content %}` (line 2)

### Template: make-post.html
- **Rendered by**: `add_new_post()` and `edit_post(post_id)` at main.py lines 231, 253
- **Context variables passed**: `form` (CreatePostForm), `current_user`, `is_edit` (boolean, for edit mode)
- **Template location**: `templates/make-post.html`
- **Imports**: `render_form` from bootstrap5/form.html (line 1)
- **Includes**: header.html (line 3), footer.html (line 39)
- **Background image**: `../static/assets/img/edit-bg.jpg` (line 8)
- **CKEditor integration**: Loaded and configured (lines 32-33)
- **Conditional heading**: Shows "Edit Post" or "New Post" based on `is_edit` (lines 14-18)
- **Block**: Uses `{% block content %}` (line 2)

### Template: about.html
- **Rendered by**: `about()` at main.py line 268
- **Context variables passed**: `current_user`
- **Template location**: `templates/about.html`
- **Includes**: header.html (line 1), footer.html (line 47)
- **Background image**: `../static/assets/img/about-bg.jpg` (line 6)

### Template: contact.html
- **Rendered by**: `contact()` at main.py line 273
- **Context variables passed**: `current_user`
- **Template location**: `templates/contact.html`
- **Includes**: header.html (line 1), footer.html (line 100)
- **Background image**: `../static/assets/img/contact-bg.jpg` (line 6)
- **Note**: Form is marked as "NOT USED in Day 69" (line 91)

### Template Inheritance
- **No template inheritance using {% extends %}** - Uses {% include %} instead
- **Shared components**: header.html and footer.html included in all pages
- **Blocks**: register.html, login.html, make-post.html use `{% block content %}` but no base template
- **Bootstrap-Flask integration**: Uses `render_form` macro from bootstrap5/form.html

### Context Data Flow
```
Python → Template Context
├── main.py line 189: all_posts=posts, current_user=current_user → index.html
│   └── posts (list of BlogPost objects) → {% for post in all_posts %}
│
├── main.py line 153: form=form, current_user=current_user → register.html
│   └── RegisterForm → {{ render_form(form) }}
│
├── main.py line 176: form=form, current_user=current_user → login.html
│   └── LoginForm → {{ render_form(form) }}
│
├── main.py line 211: post=requested_post, current_user=current_user, form=comment_form → post.html
│   ├── requested_post (BlogPost object) → {{ post.title }}, {{ post.body|safe }}
│   └── CommentForm → {{ render_form(form) }}
│
├── main.py line 231: form=form, current_user=current_user → make-post.html (new post)
│   └── CreatePostForm → {{ render_form(form) }}
│
├── main.py line 253: form=edit_form, is_edit=True, current_user=current_user → make-post.html (edit)
│   └── CreatePostForm (pre-filled) → {{ render_form(form) }}
│
├── main.py line 268: current_user=current_user → about.html
│
└── main.py line 273: current_user=current_user → contact.html
```

---

## 3. Template Loop Analysis

### index.html Loop (lines 24-43)
```jinja2
{% for post in all_posts %}
    <div class="post-preview">
        <a href="{{ url_for('show_post', post_id=post.id) }}">
            <h2 class="post-title">{{ post.title }}</h2>
            <h3 class="post-subtitle">{{ post.subtitle }}</h3>
        </a>
        <p class="post-meta">
            Posted by
            <a href="#">{{post.author.name}}</a>
            on {{post.date}}
            {% if current_user.id == 1: %}
            <a href="{{url_for('delete_post', post_id=post.id) }}">✘</a>
            {% endif %}
        </p>
    </div>
    <hr class="my-4" />
{% endfor %}
```

**Loop Details:**
- **Data source**: `all_posts` (list of BlogPost objects)
- **Provided by**: `get_all_posts()` function at main.py line 187-188
- **Iteration variable**: `post` (individual BlogPost object)
- **Variables available inside loop**:
  - `post.id` - Post ID (used in URL generation)
  - `post.title` - Post title
  - `post.subtitle` - Post subtitle
  - `post.author.name` - Author name (via relationship)
  - `post.date` - Post date
  - `post.body` - Post body (not used in this template)
  - `post.img_url` - Post image URL (not used in this template)
  - `post.comments` - Comments (not used in this template)
- **HTML elements rendered per iteration**:
  - `<div class="post-preview">` wrapper
  - `<a href="{{ url_for('show_post', post_id=post.id) }}">` link to individual post
  - `<h2 class="post-title">{{ post.title }}</h2>` - Post title heading
  - `<h3 class="post-subtitle">{{ post.subtitle }}</h3>` - Post subtitle heading
  - `<p class="post-meta">` - Post metadata
  - `<a href="#">{{post.author.name}}</a>` - Author name link
  - `on {{post.date}}` - Date display
  - Conditional delete button for admin (lines 36-38)
  - `<hr class="my-4" />` - Divider between posts

### post.html Loop (lines 51-63)
```jinja2
{% for comment in post.comments: %}
    <li>
        <div class="commenterImage">
            <img src="{{ comment.comment_author.email | gravatar }}" />
        </div>
        <div class="commentText">
            {{comment.text|safe}}
            <span class="sub-text">{{comment.comment_author.name}}</span>
        </div>
    </li>
{% endfor %}
```

**Loop Details:**
- **Data source**: `post.comments` (list of Comment objects via relationship)
- **Provided by**: `show_post(post_id)` function at main.py line 195
- **Iteration variable**: `comment` (individual Comment object)
- **Variables available inside loop**:
  - `comment.id` - Comment ID (not used)
  - `comment.text` - Comment text
  - `comment.comment_author` - User object (via relationship)
  - `comment.comment_author.email` - Author email (for Gravatar)
  - `comment.comment_author.name` - Author name
  - `comment.post_id` - Post ID (not used)
  - `comment.parent_post` - BlogPost object (not used)
- **HTML elements rendered per iteration**:
  - `<li>` - List item
  - `<div class="commenterImage">` - Image container
  - `<img src="{{ comment.comment_author.email | gravatar }}" />` - Gravatar image
  - `<div class="commentText">` - Text container
  - `{{comment.text|safe}}` - Comment text (safe HTML)
  - `<span class="sub-text">{{comment.comment_author.name}}</span>` - Author name

### login.html Loop (lines 28-30)
```jinja2
{% for message in messages %}
    <p class="flash">{{ message }}</p>
{% endfor %}
```

**Loop Details:**
- **Data source**: `messages` (list of flash messages)
- **Provided by**: `get_flashed_messages()` at line 26
- **Iteration variable**: `message` (individual flash message string)
- **Variables available inside loop**:
  - `message` - Flash message text
- **HTML elements rendered per iteration**:
  - `<p class="flash">{{ message }}</p>` - Flash message paragraph

### about.html
- **No loops present** - Static content page

### contact.html
- **No loops present** - Form-based page (not functional in this version)

### register.html
- **No loops present** - Form-based page

### make-post.html
- **No loops present** - Form-based page

### header.html
- **No loops present** - Navigation and header

### footer.html
- **No loops present** - Footer and scripts

---

## 4. Static File References

### CSS File References

#### header.html (line 14)
```html
{{ bootstrap.load_css() }}
```
- **CSS file**: Bootstrap-Flask CSS (loaded via Bootstrap5 extension)
- **Purpose**: Bootstrap 5 CSS framework

#### header.html (line 38)
```html
<link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet" />
```
- **CSS file**: `static/css/styles.css`
- **Path reference**: Flask url_for helper
- **Purpose**: Custom Clean Blog theme CSS

### JavaScript File References

#### footer.html (line 38)
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
```
- **JavaScript file**: Bootstrap bundle from CDN
- **Purpose**: Bootstrap JavaScript components (modals, dropdowns, etc.)

#### footer.html (line 40)
```html
<script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
```
- **JavaScript file**: `static/js/scripts.js`
- **Path reference**: Flask url_for helper
- **Purpose**: Custom navigation scroll behavior

### CKEditor JavaScript

#### post.html (lines 43-45)
```html
{{ ckeditor.load() }}
{{ ckeditor.config(name='comment_text') }}
```
- **JavaScript**: CKEditor rich text editor
- **Purpose**: WYSIWYG editor for comments

#### make-post.html (lines 32-33)
```html
{{ ckeditor.load() }}
{{ ckeditor.config(name='body') }}
```
- **JavaScript**: CKEditor rich text editor
- **Purpose**: WYSIWYG editor for blog post body

### CSS Classes Used (Bootstrap + Custom)

#### Bootstrap Classes (from Bootstrap-Flask)
**Grid System:**
- `.container` - Container for content
- `.row` - Row for grid layout
- `.col-md-10`, `.col-lg-8`, `.col-xl-7` - Column breakpoints
- `.col-lg-8`, `.col-md-10`, `.mx-auto` - Column layout for forms
- `.px-4`, `.px-lg-5` - Padding utilities
- `.gx-4`, `.gx-lg-5` - Gutter utilities

**Navigation:**
- `.navbar` - Navbar container
- `.navbar-expand-lg` - Responsive navbar
- `.navbar-light` - Light theme
- `.navbar-brand` - Brand/logo
- `.navbar-toggler` - Mobile toggle button
- `.navbar-nav` - Navigation links
- `.nav-item` - Navigation item
- `.nav-link` - Navigation link
- `.ms-auto` - Margin start auto

**Typography:**
- `.site-heading` - Site heading
- `.subheading` - Subheading text
- `.post-title` - Post title styling
- `.post-subtitle` - Post subtitle styling
- `.post-meta` - Post metadata
- `.page-heading` - Page heading
- `.post-heading` - Individual post heading

**Components:**
- `.post-preview` - Post preview card
- `.btn` - Button base
- `.btn-primary` - Primary button
- `.btn-secondary` - Secondary button
- `.btn-danger` - Danger button
- `.text-uppercase` - Uppercase text
- `.mb-4` - Margin bottom
- `.my-4` - Margin vertical
- `.my-5` - Margin vertical (larger)
- `.mb-4` - Margin bottom
- `.d-flex` - Display flex
- `.justify-content-end` - Flex alignment
- `.float-right` - Float right

**Forms:**
- `.form-floating` - Floating label form group
- `.form-control` - Form input styling
- `.border-top` - Border top

**Footer:**
- `.list-inline` - Inline list
- `.list-inline-item` - Inline list item
- `.fa-stack` - Font icon stack
- `.text-center` - Center text
- `.text-muted` - Muted text
- `.fst-italic` - Italic text
- `.small` - Small text

**Comments:**
- `.comment` - Comment container
- `.commentList` - Comment list
- `.commenterImage` - Comment author image
- `.commentText` - Comment text container
- `.sub-text` - Subtitle text

**Flash Messages:**
- `.flash` - Flash message styling

### External Resources

#### Font Awesome (header.html lines 21-24)
```html
<script src="https://use.fontawesome.com/releases/v6.3.0/js/all.js" crossorigin="anonymous"></script>
```
- **Purpose**: Font Awesome icon library
- **Used for**: Social media icons in footer (Twitter, Facebook, GitHub)

#### Google Fonts (header.html lines 26-35)
```html
<link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
<link href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css" />
```
- **Purpose**: Load Lora and Open Sans font families
- **Applied to**: Body text and headings via CSS

#### Favicon (header.html lines 16-19)
```html
<link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='assets/favicon.ico') }}" />
```
- **File**: `static/assets/favicon.ico`
- **Purpose**: Browser tab icon

### Image/Asset References

#### index.html (line 6)
```html
style="background-image: url('../static/assets/img/home-bg.jpg')"
```
- **Image file**: `static/assets/img/home-bg.jpg`
- **Purpose**: Homepage header background

#### post.html (line 5)
```html
style="background-image: url('{{post.img_url}}')"
```
- **Image source**: Dynamic from post data
- **Purpose**: Individual post header background

#### register.html (line 7)
```html
style="background-image: url('../static/assets/img/register-bg.jpg')"
```
- **Image file**: `static/assets/img/register-bg.jpg`
- **Purpose**: Register page header background

#### login.html (line 8)
```html
style="background-image: url('../static/assets/img/login-bg.jpg')"
```
- **Image file**: `static/assets/img/login-bg.jpg`
- **Purpose**: Login page header background

#### make-post.html (line 8)
```html
style="background-image: url('../static/assets/img/edit-bg.jpg')"
```
- **Image file**: `static/assets/img/edit-bg.jpg`
- **Purpose**: Edit/Create post page header background

#### about.html (line 6)
```html
style="background-image: url('../static/assets/img/about-bg.jpg')"
```
- **Image file**: `static/assets/img/about-bg.jpg`
- **Purpose**: About page header background

#### contact.html (line 6)
```html
style="background-image: url('../static/assets/img/contact-bg.jpg')"
```
- **Image file**: `static/assets/img/contact-bg.jpg`
- **Purpose**: Contact page header background

#### Gravatar Images (post.html line 55)
```html
<img src="{{ comment.comment_author.email | gravatar }}" />
```
- **Image source**: Gravatar service (dynamic based on email)
- **Purpose**: Comment author profile images

---

## 5. Data Flow Diagram

```mermaid
graph TD
    A[User Request] --> B{Route Matching}
    B -->|/| C[get_all_posts]
    B -->|/register GET/POST| D[register]
    B -->|/login GET/POST| E[login]
    B -->|/logout| F[logout]
    B -->|/post/&lt;post_id&gt; GET/POST| G[show_post post_id]
    B -->|/new-post GET/POST| H[add_new_post]
    B -->|/edit-post/&lt;post_id&gt; GET/POST| I[edit_post post_id]
    B -->|/delete/&lt;post_id&gt;| J[delete_post post_id]
    B -->|/about| K[about]
    B -->|/contact| L[contact]
    
    C --> M[render_template index.html]
    D --> N[render_template register.html]
    E --> O[render_template login.html]
    F --> P[redirect get_all_posts]
    G --> Q[render_template post.html]
    H --> R[render_template make-post.html]
    I --> R
    J --> P
    K --> S[render_template about.html]
    L --> T[render_template contact.html]
    
    M --> U[Return HTML Response]
    N --> U
    O --> U
    P --> C
    Q --> U
    R --> U
    S --> U
    T --> U
    
    D --> V{POST Request?}
    V -->|Yes| W[validate_on_submit]
    V -->|No| N
    W --> X{Email exists?}
    X -->|Yes| Y[flash error]
    X -->|No| Z[hash password]
    Y --> P
    Z --> AA[create User]
    AA --> AB[db.session.add]
    AB --> AC[db.session.commit]
    AC --> AD[login_user]
    AD --> P
    
    E --> AE{POST Request?}
    AE -->|Yes| AF[validate_on_submit]
    AE -->|No| O
    AF --> AG[check credentials]
    AG --> AH{Valid?}
    AH -->|No| AI[flash error]
    AH -->|Yes| AJ[login_user]
    AI --> P
    AJ --> P
    
    G --> AK{POST Request?}
    AK -->|Yes| AL[validate_on_submit]
    AK -->|No| Q
    AL --> AM{Authenticated?}
    AM -->|No| AN[flash error]
    AM -->|Yes| AO[create Comment]
    AN --> P
    AO --> AP[db.session.add]
    AP --> AQ[db.session.commit]
    AQ --> Q
    
    H --> AR{@admin_only}
    AR --> AS{User id == 1?}
    AS -->|No| AT[abort 403]
    AS -->|Yes| AU[validate_on_submit]
    AU --> AV[create BlogPost]
    AV --> AW[db.session.add]
    AW --> AX[db.session.commit]
    AX --> P
    
    I --> AR
    AU --> AY[update BlogPost]
    AY --> AX
    
    J --> AR
    AS -->|Yes| AZ[delete BlogPost]
    AZ --> BA[db.session.commit]
    BA --> P
    
    BB[SQLite Database posts.db] --> BC[BlogPost table]
    BB --> BD[User table]
    BB --> BE[Comment table]
    
    BC --> C
    BC --> G
    BC --> H
    BC --> I
    BC --> J
    
    BD --> D
    BD --> E
    BD --> F
    BD --> G
    
    BE --> G
    
    BF[static/css/styles.css] --> BG[CSS Styling]
    BG --> U
    
    BH[static/js/scripts.js] --> BI[Navigation Behavior]
    BI --> U
    
    BJ[Bootstrap CDN JS] --> BK[Bootstrap Components]
    BK --> U
    
    BL[CKEditor] --> BM[Rich Text Editor]
    BM --> Q
    BM --> R
    
    BN[Gravatar] --> BO[Profile Images]
    BO --> Q
    
    style C fill:#e1f5ff
    style D fill:#e1f5ff
    style E fill:#e1f5ff
    style G fill:#e1f5ff
    style H fill:#e1f5ff
    style I fill:#e1f5ff
    style K fill:#e1f5ff
    style L fill:#e1f5ff
    style M fill:#fff4e1
    style N fill:#fff4e1
    style O fill:#fff4e1
    style Q fill:#fff4e1
    style R fill:#fff4e1
    style S fill:#fff4e1
    style T fill:#fff4e1
    style U fill:#e8f5e9
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
│   /     │         │/register│         │ /login       │  │/logout   │
│get_all_ │         │register()│         │ login()      │  │logout()  │
│ posts() │         └────┬────┘         └──────┬───────┘  └────┬─────┘
└────┬────┘              │                     │               │
     │                   │                     │               │
     │                   ▼                     ▼               ▼
     │            ┌──────────────┐     ┌──────────────┐   ┌──────────┐
     │            │ POST?        │     │ POST?        │   │logout_user│
     │            └──────┬───────┘     └──────┬───────┘   │redirect  │
     │              Yes │              Yes │            │to home   │
     │                   ▼                   ▼            └──────────┘
     │            ┌──────────────┐   ┌──────────────┐
     │            │validate form │   │validate form │
     │            └──────┬───────┘   └──────┬───────┘
     │                   │                   │
     │                   ▼                   ▼
     │            ┌──────────────┐   ┌──────────────┐
     │            │check email   │   │check email   │
     │            │exists?       │   │& password    │
     │            └──────┬───────┘   └──────┬───────┘
     │                   │                   │
     │            ┌──────┴───────┐   ┌──────┴───────┐
     │            │              │   │              │
     │            ▼              ▼   ▼              ▼
     │       ┌─────────┐  ┌─────────┐  ┌─────────┐
     │       │hash pwd │  │flash err│  │login_user│
     │       │create   │  │redirect │  │redirect │
     │       │User     │  │to login │  │to home  │
     │       └────┬────┘  └─────────┘  └─────────┘
     │            │
     │            ▼
     │       ┌─────────┐
     │       │save to  │
     │       │DB       │
     │       └────┬────┘
     │            │
     └────────────┴─────────────┬───────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │render_template   │
                    │index.html        │
                    │all_posts=posts   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │Include header    │
                    │Include footer    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  HTML Response   │
                    │  + CSS Styling   │
                    │  + JavaScript    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Browser Render │
                    └──────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    DATABASE RELATIONSHIPS                         │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐
│    User      │
│  (users)     │
└──────┬───────┘
       │ id
       │
       ├──────────────────────┐
       │                      │
       ▼                      ▼
┌──────────────┐      ┌──────────────┐
│  BlogPost    │      │  Comment     │
│ (blog_posts) │      │ (comments)   │
└──────┬───────┘      └──────┬───────┘
       │                     │
       │ author_id            │ author_id
       │                     │
       │                     │
       ├─────────────────────┘
       │
       │ post_id
       ▼
┌──────────────┐
│  Comment     │
│ (comments)   │
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
│  to home     │
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
│  to home     │
└──────────────┘
```

---

## 6. Written Summary

### Application Architecture
This is a **full-featured Flask blog application with user authentication, database persistence, and commenting system** following the **Model-View-Controller (MVC)** pattern:
- **Model**: SQLAlchemy ORM models (BlogPost, User, Comment) with relationships
- **View**: HTML templates in `templates/` with shared header/footer components
- **Controller**: Flask routes in `main.py` - Business logic, authentication, CRUD operations

### Request Lifecycle Walkthrough

#### 1. Application Startup
1. Python executes `main.py`
2. Imports all dependencies (Flask, extensions, forms, SQLAlchemy)
3. Initializes Flask application with SECRET_KEY (line 29-30)
4. Configures CKEditor and Bootstrap5 extensions (lines 31-32)
5. Configures Flask-Login for authentication (lines 34-41)
6. Configures Gravatar for profile images (lines 44-52)
7. Configures SQLite database (line 57)
8. Defines database models: BlogPost, User, Comment (lines 63-104)
9. Creates database tables if they don't exist (lines 107-108)
10. Starts development server on port 5001 with debug mode (line 277)

#### 2. Homepage Request (`/`)
1. User navigates to `http://localhost:5001/`
2. Flask router matches route to `get_all_posts()` function
3. Function queries database for all blog posts (line 187-188)
4. Renders `index.html` with `all_posts=posts` and `current_user` context
5. Template includes `header.html` and `footer.html`
6. Template iterates through posts using Jinja2 loop
7. Each post displays title, subtitle, author name, and date
8. Admin-only delete button shown if `current_user.id == 1`
9. Admin-only "Create New Post" button shown if user is admin
10. Bootstrap CSS and custom styles applied
11. HTML response returned to browser

#### 3. Registration Request (`/register`)
1. User clicks "Register" link in navigation
2. Flask router matches route to `register()` function
3. **GET request**: Renders `register.html` with RegisterForm
4. Template includes `header.html` and `footer.html`
5. Registration form displayed with email, password, name fields
6. **POST request** (form submission):
   - Form validation via WTForms (line 128)
   - Checks if email already exists in database (line 131-132)
   - If exists: flashes error and redirects to login (line 135-136)
   - If new: hashes password using pbkdf2:sha256 (line 138-142)
   - Creates new User object (line 143-147)
   - Saves to database (line 148-149)
   - Authenticates user with Flask-Login (line 151)
   - Redirects to homepage (line 152)
7. HTML response returned to browser

#### 4. Login Request (`/login`)
1. User clicks "Login" link in navigation
2. Flask router matches route to `login()` function
3. **GET request**: Renders `login.html` with LoginForm
4. Template includes `header.html` and `footer.html`
5. Login form displayed with email, password fields
6. **POST request** (form submission):
   - Form validation via WTForms (line 159)
   - Queries database for user by email (line 161-163)
   - If email doesn't exist: flashes error and redirects to login (line 165-167)
   - If password incorrect: flashes error and redirects to login (line 169-171)
   - If credentials valid: authenticates user with Flask-Login (line 173)
   - Redirects to homepage (line 174)
7. Flash messages displayed for errors (lines 26-32 in template)
8. HTML response returned to browser

#### 5. Logout Request (`/logout`)
1. User clicks "Log Out" link in navigation
2. Flask router matches route to `logout()` function
3. Function calls `logout_user()` from Flask-Login (line 181)
4. Redirects to homepage (line 182)
5. Navigation now shows Login/Register links instead of Logout

#### 6. Individual Post Request (`/post/<post_id>`)
1. User clicks post title on homepage
2. URL generated: `/post/<post.id>` using `url_for()`
3. Flask router matches dynamic route to `show_post(post_id)` function
4. Function queries database for post by ID (line 195)
5. Creates CommentForm instance (line 197)
6. **GET request**: Renders `post.html` with post, current_user, and form context
7. Template includes `header.html` and `footer.html`
8. Template displays post with background image, title, subtitle, author, date, and body
9. CKEditor loaded for comment form (lines 43-45)
10. Admin-only "Edit Post" button shown if user is admin (lines 31-39)
11. All comments displayed with Gravatar images (lines 48-64)
12. **POST request** (comment submission):
    - Form validation (line 199)
    - Checks if user is authenticated (line 200)
    - If not authenticated: flashes error and redirects to login (line 201-202)
    - If authenticated: creates new Comment object (line 204-208)
    - Saves to database (line 209-210)
    - Re-renders page with new comment
13. HTML response returned to browser

#### 7. Create New Post Request (`/new-post`)
1. Admin user clicks "Create New Post" button on homepage
2. Flask router matches route to `add_new_post()` function
3. **@admin_only decorator** checks if user.id == 1 (line 216)
4. If not admin: returns 403 Forbidden
5. **GET request**: Renders `make-post.html` with CreatePostForm
6. Template includes `header.html` and `footer.html`
7. CKEditor loaded for body field (lines 32-33)
8. Form displays title, subtitle, image URL, and body fields
9. **POST request** (form submission):
    - Form validation (line 219)
    - Creates new BlogPost object with form data (line 220-227)
    - Sets author to current_user
    - Sets date to today's date (line 226)
    - Saves to database (line 228-229)
    - Redirects to homepage (line 230)
10. HTML response returned to browser

#### 8. Edit Post Request (`/edit-post/<post_id>`)
1. Admin user clicks "Edit Post" button on post page
2. Flask router matches dynamic route to `edit_post(post_id)` function
3. **@admin_only decorator** checks if user.id == 1
4. Function queries database for post by ID (line 237)
5. Creates CreatePostForm pre-filled with post data (line 238-244)
6. **GET request**: Renders `make-post.html` with form and `is_edit=True`
7. Template shows "Edit Post" heading instead of "New Post" (lines 14-18)
8. **POST request** (form submission):
    - Form validation (line 245)
    - Updates post fields with form data (lines 246-250)
    - Saves changes to database (line 251)
    - Redirects to post page (line 252)
9. HTML response returned to browser

#### 9. Delete Post Request (`/delete/<post_id>`)
1. Admin user clicks delete button (✘) on homepage
2. Flask router matches dynamic route to `delete_post(post_id)` function
3. **@admin_only decorator** checks if user.id == 1
4. Function queries database for post by ID (line 260)
5. Deletes post from database (line 261)
6. Commits transaction (line 262)
7. Redirects to homepage (line 263)
8. Post no longer appears in post list

#### 10. About Page Request (`/about`)
1. User clicks "About" link in navigation
2. Flask router matches route to `about()` function
3. Function renders `about.html` with `current_user` context
4. Template includes `header.html` and `footer.html`
5. Static content displayed with Lorem ipsum text
6. HTML response returned to browser

#### 11. Contact Page Request (`/contact`)
1. User clicks "Contact" link in navigation
2. Flask router matches route to `contact()` function
3. Function renders `contact.html` with `current_user` context
4. Template includes `header.html` and `footer.html`
5. Contact form displayed but marked as "NOT USED in Day 69" (line 91)
6. No form handling implemented in this version
7. HTML response returned to browser

### Key Files and Responsibilities

#### main.py (9825 bytes)
- **Lines 1-14**: Import statements
- **Lines 29-32**: Flask app initialization and extensions
- **Lines 34-41**: Flask-Login configuration
- **Lines 44-52**: Gravatar configuration
- **Lines 54-109**: Database configuration and models
- **Lines 112-121**: admin_only decorator
- **Lines 125-153**: Registration route
- **Lines 156-176**: Login route
- **Lines 179-182**: Logout route
- **Lines 185-189**: Homepage route
- **Lines 193-211**: Individual post route with comments
- **Lines 215-231**: Create new post route
- **Lines 235-253**: Edit post route
- **Lines 257-263**: Delete post route
- **Lines 266-268**: About page route
- **Lines 271-273**: Contact page route
- **Lines 276-277**: Application startup

#### forms.py (1305 bytes)
- **Lines 1-4**: Import statements
- **Lines 8-13**: CreatePostForm - Blog post creation/editing
- **Lines 17-21**: RegisterForm - User registration
- **Lines 25-28**: LoginForm - User login
- **Lines 32-34**: CommentForm - Comment submission

#### requirements.txt (198 bytes)
- **Bootstrap_Flask==2.2.0**: Bootstrap integration
- **Flask_CKEditor==0.4.6**: Rich text editor
- **Flask_Login==0.6.3**: User authentication
- **Flask-Gravatar==0.5.0**: Profile images
- **Flask_WTF==1.2.1**: Form handling
- **WTForms==3.0.1**: Form validation
- **Werkzeug==3.0.0**: Password hashing
- **Flask==2.3.2**: Web framework
- **flask_sqlalchemy==3.1.1**: ORM
- **SQLAlchemy==2.0.25**: Database toolkit

#### templates/header.html (3473 bytes)
- **Lines 1-42**: HTML head with Bootstrap, fonts, CSS
- **Lines 44-111**: Navigation bar with authentication logic
- **Purpose**: Shared header component for all pages

#### templates/footer.html (2118 bytes)
- **Lines 1-36**: Footer with social media icons
- **Lines 37-42**: Bootstrap JS and custom scripts
- **Purpose**: Shared footer component for all pages

#### templates/index.html (2021 bytes)
- **Line 1**: Include header
- **Lines 3-18**: Page header
- **Lines 20-63**: Main content with post loop
- **Lines 24-43**: Post preview loop with admin controls
- **Lines 47-55**: Admin-only create post button
- **Line 65**: Include footer

#### templates/post.html (2330 bytes)
- **Line 1**: Import render_form macro
- **Line 2**: Include header
- **Lines 4-22**: Page header with dynamic background
- **Lines 25-30**: Post content display
- **Lines 31-39**: Admin-only edit button
- **Lines 43-47**: CKEditor and comment form
- **Lines 48-66**: Comments loop with Gravatar
- **Line 72**: Include footer

#### templates/register.html (1169 bytes)
- **Line 1**: Import render_form macro
- **Lines 3-19**: Page header
- **Lines 21-30**: Registration form
- **Line 32**: Include footer

#### templates/login.html (913 bytes)
- **Line 1**: Import render_form macro
- **Lines 5-20**: Page header
- **Lines 22-39**: Login form with flash messages
- **Line 42**: Include footer

#### templates/make-post.html (1106 bytes)
- **Line 1**: Import render_form macro
- **Lines 5-26**: Page header with conditional heading
- **Lines 28-38**: Post form with CKEditor
- **Line 39**: Include footer

#### templates/about.html (1603 bytes)
- **Line 1**: Include header
- **Lines 3-18**: Page header
- **Lines 20-45**: Static content
- **Line 47**: Include footer

#### templates/contact.html (3020 bytes)
- **Line 1**: Include header
- **Lines 3-22**: Page header
- **Lines 24-98**: Contact form (not functional)
- **Line 100**: Include footer

### Configuration
- **Debug mode**: Enabled (`debug=True`)
- **Host**: Default (127.0.0.1)
- **Port**: 5001 (custom)
- **Template folder**: `templates/` (Flask default)
- **Static folder**: `static/` (Flask default)
- **Database**: SQLite (`sqlite:///posts.db`)
- **SECRET_KEY**: '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
- **Admin user**: User with id=1

### Database
- **Type**: SQLite
- **Location**: `instance/posts.db`
- **ORM**: SQLAlchemy 2.0.25
- **Tables**:
  - `users`: id, email, password (hashed), name
  - `blog_posts`: id, author_id (FK), title, subtitle, date, body, img_url
  - `comments`: id, text, author_id (FK), post_id (FK)
- **Relationships**:
  - User → BlogPost: One-to-many (author to posts)
  - User → Comment: One-to-many (comment_author to comments)
  - BlogPost → Comment: One-to-many (parent_post to comments)
- **Data persistence**: Persistent (SQLite file)

### Security Considerations
- Password hashing using pbkdf2:sha256 with salt (line 138-142)
- User authentication via Flask-Login
- Admin-only decorator for sensitive operations (lines 112-121)
- CSRF protection via Flask-WTF
- SECRET_KEY configured for session security
- Input validation via WTForms
- SQL injection protection via SQLAlchemy ORM
- No HTTPS enforcement
- Debug mode enabled (not production-ready)
- Admin check based on hardcoded id=1 (not scalable)

### Technology Stack
- **Framework**: Flask 2.3.2 (Python web framework)
- **ORM**: SQLAlchemy 2.0.25 with Flask-SQLAlchemy
- **Authentication**: Flask-Login 0.6.3
- **Forms**: Flask-WTF 1.2.1 with WTForms 3.0.1
- **Password Security**: Werkzeug 3.0.0
- **CSS Framework**: Bootstrap 5 via Bootstrap-Flask 2.2.0
- **Rich Text Editor**: Flask-CKEditor 0.4.6
- **Profile Images**: Flask-Gravatar 0.5.0
- **Templating**: Jinja2 (Flask's default)
- **Database**: SQLite
- **Icons**: Font Awesome 6.3.0
- **Fonts**: Google Fonts (Lora, Open Sans)

### External Dependencies
- **Bootstrap 5.2.3**: CSS framework (via Bootstrap-Flask)
- **Bootstrap JS**: Loaded from CDN (jsdelivr)
- **Font Awesome**: Loaded from CDN (use.fontawesome.com)
- **Google Fonts**: Loaded from fonts.googleapis.com
- **Gravatar**: Profile image service (gravatar.com)
- **CKEditor**: Rich text editor (loaded via Flask-CKEditor)

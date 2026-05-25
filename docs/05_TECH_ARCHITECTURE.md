# 05 — TECH ARCHITECTURE & DEPLOYMENT

---

## FLASK APP STRUCTURE

### `config.py`
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-in-prod')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///green_experience.db')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
```

### `app/__init__.py` (App Factory)
```python
from flask import Flask
from .routes.main import main_bp
from .routes.auth import auth_bp
from .routes.booking import booking_bp
from .routes.dashboard import dashboard_bp
from .routes.admin import admin_bp
import sqlite3, os

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)

    # Init DB
    with app.app_context():
        init_db(app)

    return app

def init_db(app):
    db_path = os.path.join(app.instance_path, 'green_experience.db')
    os.makedirs(app.instance_path, exist_ok=True)
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        with open('db/schema.sql') as f:
            conn.executescript(f.read())
        conn.close()
```

### `run.py`
```python
from app import create_app
import os

app = create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

## JINJA2 TEMPLATE PATTERNS

### `base.html` skeleton
```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Green Experience – Responsible Journey{% endblock %}</title>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Be+Vietnam+Pro:wght@300;400;500;600&display=swap" rel="stylesheet">

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>

  <!-- Global CSS -->
  <link rel="stylesheet" href="{{ url_for('static', filename='css/global.css') }}">

  <!-- Page-specific CSS -->
  {% block extra_css %}{% endblock %}
</head>
<body>
  <!-- Navigation -->
  {% include 'partials/nav.html' %}

  <!-- Flash messages -->
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
      <div class="flash-container">
        {% for category, message in messages %}
          <div class="flash flash-{{ category }}">{{ message }}</div>
        {% endfor %}
      </div>
    {% endif %}
  {% endwith %}

  <!-- Main content -->
  <main>
    {% block content %}{% endblock %}
  </main>

  <!-- Footer -->
  {% include 'partials/footer.html' %}

  <!-- Lucide init -->
  <script>lucide.createIcons();</script>

  <!-- Global JS -->
  <script src="{{ url_for('static', filename='js/main.js') }}"></script>

  {% block extra_js %}{% endblock %}
</body>
</html>
```

### Jinja2 loops cho destinations
```html
<!-- destinations.html -->
{% extends 'base.html' %}
{% block content %}
  <div class="destinations-grid reveal-group">
    {% for dest in destinations %}
      <article class="dest-card reveal theme-{{ dest.id | replace('-','_') }}">
        <div class="dest-card__img-wrap">
          <img src="{{ dest.image }}" alt="{{ dest.name }}" loading="lazy">
          <div class="dest-card__overlay"></div>
          <span class="dest-card__region">{{ dest.region }}</span>
        </div>
        <div class="dest-card__body">
          <span class="tag">{{ dest.tagline }}</span>
          <h3>{{ dest.name }}</h3>
          <p>{{ dest.description[:120] }}...</p>
          <div class="dest-card__stats">
            <span>📅 {{ dest.days }}</span>
            <span>💰 Từ {{ "{:,.0f}".format(dest.priceFrom).replace(',','.') }} ₫</span>
            <span class="gp-badge">+{{ dest.greenPoints }} GP</span>
          </div>
          <a href="/destinations/{{ dest.id }}" class="btn btn-primary">Xem hành trình →</a>
        </div>
      </article>
    {% endfor %}
  </div>
{% endblock %}
```

### Format tiền Việt Nam trong Jinja2
```python
# Đăng ký filter trong app/__init__.py
@app.template_filter('vnd')
def vnd_filter(amount):
    return f"{amount:,.0f}".replace(',', '.') + ' ₫'
```
```html
{{ tour.price | vnd }}  → "4.500.000 ₫"
```

---

## SESSION & AUTH PATTERN

```python
# routes/auth.py
from flask import Blueprint, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db.helpers import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['is_admin'] = bool(user['is_admin'])
            flash('Chào mừng trở lại! 🌿', 'success')
            return redirect('/dashboard')
        flash('Email hoặc mật khẩu không đúng', 'error')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Decorator for protected routes
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('Vui lòng đăng nhập để tiếp tục', 'info')
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated
```

---

## DEPLOY ON RENDER.COM

### `requirements.txt`
```
Flask==3.0.3
Werkzeug==3.0.3
gunicorn==22.0.0
python-dotenv==1.0.1
```

### `Procfile`
```
web: gunicorn run:app
```

### `render.yaml`
```yaml
services:
  - type: web
    name: green-experience
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn run:app
    envVars:
      - key: SECRET_KEY
        generateValue: true
      - key: FLASK_ENV
        value: production
    disk:
      name: sqlite-data
      mountPath: /app/instance
      sizeGB: 1
```

> **Quan trọng**: Render free tier có persistent disk $0/month nhưng cần enable.
> SQLite file lưu tại `/app/instance/green_experience.db` (trong disk mount).

### `.gitignore`
```
instance/
__pycache__/
*.pyc
.env
*.db
```

### `.env` (local dev only)
```
SECRET_KEY=your-dev-secret-key
FLASK_ENV=development
```

---

## LOCAL DEVELOPMENT SETUP

```bash
# 1. Tạo virtual env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Khởi tạo DB lần đầu (tự động khi chạy app)
python run.py

# 4. Tạo admin user (chạy 1 lần)
python -c "
from app import create_app
from db.helpers import get_db
from werkzeug.security import generate_password_hash
app = create_app()
with app.app_context():
    db = get_db()
    db.execute(
        'INSERT INTO users (name, email, password_hash, is_admin) VALUES (?,?,?,?)',
        ('Admin', 'admin@green.vn', generate_password_hash('admin123'), 1)
    )
    db.commit()
    print('Admin created!')
"

# 5. Run
python run.py
# → http://localhost:5000
```

---

## STEP-BY-STEP IMPLEMENTATION ORDER

### Bước 1: Setup project (30 min)
```
□ Tạo folder structure (xem 01_PROJECT_CONTEXT.md)
□ Tạo virtual env + requirements.txt
□ Tạo config.py + app/__init__.py
□ Tạo db/schema.sql (xem 04_DATABASE_SCHEMA.md)
□ Tạo run.py
□ Test: python run.py → 200 OK
```

### Bước 2: Design tokens + Base (45 min)
```
□ Tạo static/css/global.css (paste từ 02_DESIGN_SYSTEM.md)
□ Tạo templates/base.html (nav + footer + flash)
□ Tạo templates/partials/nav.html
□ Tạo templates/partials/footer.html
□ Test: render base template không lỗi
```

### Bước 3: Static data + Home (60 min)
```
□ Tạo data/static_data.py (convert từ mockData.ts)
□ Tạo routes/main.py với route /
□ Tạo templates/home.html (xem 03_PAGES_SPEC.md)
□ Tạo static/css/home.css
□ Test: homepage render đủ sections
```

### Bước 4: Destinations pages (60 min)
```
□ Route /destinations + /destinations/<id>
□ templates/destinations.html
□ templates/destination_detail.html
□ tours/<id> route + template
```

### Bước 5: Supporting pages (45 min)
```
□ /homestays, /community, /co2-calculator, /about
□ JS logic cho CO₂ calculator (xem 03_PAGES_SPEC.md)
```

### Bước 6: Auth (45 min)
```
□ routes/auth.py (login, register, logout)
□ templates/login.html + register.html
□ Test: register → login → session
```

### Bước 7: Booking flow (60 min)
```
□ routes/booking.py
□ templates/booking.html (3 steps)
□ SQLite insert booking + update points
□ Test: full booking flow → DB
```

### Bước 8: Dashboard + Certificate (45 min)
```
□ routes/dashboard.py (login required)
□ templates/dashboard.html (points, history, badges)
□ templates/certificate.html (print CSS)
```

### Bước 9: Admin (30 min)
```
□ routes/admin.py
□ templates/admin/bookings.html (table đơn giản)
□ templates/admin/leads.html
```

### Bước 10: Deploy (30 min)
```
□ Tạo Procfile + render.yaml
□ Push lên GitHub
□ Connect Render.com → deploy
□ Set environment variables
□ Test production
```

---

## COMMON PITFALLS

1. **SQLite path on Render**: Phải dùng absolute path `os.path.join(app.instance_path, ...)`, không phải relative
2. **Vietnamese encoding**: Đảm bảo `<meta charset="UTF-8">` và Python files có `# -*- coding: utf-8 -*-`
3. **Static files cache**: Khi dev, browser cache CSS — dùng Ctrl+Shift+R hoặc thêm version query `?v=1`
4. **Flash messages**: Cần `session.permanent = True` hoặc `SECRET_KEY` phù hợp
5. **Form CSRF**: Không bắt buộc cho MVP nhưng nên thêm `Flask-WTF` sau
6. **Image fallback**: Unsplash URLs có thể timeout — thêm CSS `background-color` fallback cho img containers

# 04 — DATABASE SCHEMA (SQLite)

> Tất cả dữ liệu tour/destination/homestay là STATIC (hardcode trong Python dict hoặc JSON file).
> SQLite chỉ lưu dữ liệu DYNAMIC: users, bookings, sessions, green_points_log.

---

## MODELS (SQLAlchemy)

### `User`
```python
class User(db.Model):
    __tablename__ = 'users'

    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    email         = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    green_points  = db.Column(db.Integer, default=0)
    level         = db.Column(db.String(50), default='Eco Beginner')
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin      = db.Column(db.Boolean, default=False)

    # Relationships
    bookings      = db.relationship('Booking', backref='user', lazy=True)
    points_log    = db.relationship('GreenPointsLog', backref='user', lazy=True)
```

### `Booking`
```python
class Booking(db.Model):
    __tablename__ = 'bookings'

    id              = db.Column(db.Integer, primary_key=True)
    booking_code    = db.Column(db.String(20), unique=True, nullable=False)

    # Tour info (denormalized từ static data)
    tour_id         = db.Column(db.String(50))      # e.g. 'lo-lo-chai-culture'
    tour_name       = db.Column(db.String(200))
    destination_id  = db.Column(db.String(50))      # e.g. 'lo-lo-chai'
    destination_name= db.Column(db.String(100))

    # Guest info
    guests          = db.Column(db.Integer, default=1)
    total_price     = db.Column(db.Integer)          # VNĐ (integer, không float)
    green_points_earned = db.Column(db.Integer, default=0)
    co2_saved       = db.Column(db.Float, default=0)
    transport_choice= db.Column(db.String(50))       # 'xe_khach', 'xe_dien', etc.

    # Customer info (có thể là guest, không cần account)
    user_id         = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    customer_name   = db.Column(db.String(100), nullable=False)
    customer_email  = db.Column(db.String(150), nullable=False)
    customer_phone  = db.Column(db.String(20))
    notes           = db.Column(db.Text)

    # Status
    status          = db.Column(db.String(20), default='pending')
    # Values: 'pending', 'confirmed', 'completed', 'cancelled'
    created_at      = db.Column(db.DateTime, default=datetime.utcnow)
    travel_date     = db.Column(db.Date, nullable=True)
```

### `GreenPointsLog`
```python
class GreenPointsLog(db.Model):
    __tablename__ = 'green_points_log'

    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action      = db.Column(db.String(100))
    # e.g. 'Đặt tour xanh', 'Check-in homestay', 'Tham gia cộng đồng'
    points      = db.Column(db.Integer)               # Positive = earn, Negative = redeem
    reference   = db.Column(db.String(50))            # booking_code hoặc activity_id
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
```

### `ContactLead` (Thu lead từ form liên hệ/tour inquiry)
```python
class ContactLead(db.Model):
    __tablename__ = 'contact_leads'

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100))
    email       = db.Column(db.String(150))
    phone       = db.Column(db.String(20))
    interest    = db.Column(db.String(100))  # Tour interested in
    message     = db.Column(db.Text)
    source      = db.Column(db.String(50))   # 'home_cta', 'tour_detail', 'co2_calc'
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
    contacted   = db.Column(db.Boolean, default=False)
```

---

## SQL (Raw — nếu không dùng SQLAlchemy)

```sql
-- init_db.sql

CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    email         TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    green_points  INTEGER DEFAULT 0,
    level         TEXT DEFAULT 'Eco Beginner',
    is_admin      INTEGER DEFAULT 0,
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bookings (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_code        TEXT UNIQUE NOT NULL,
    tour_id             TEXT,
    tour_name           TEXT,
    destination_id      TEXT,
    destination_name    TEXT,
    guests              INTEGER DEFAULT 1,
    total_price         INTEGER,
    green_points_earned INTEGER DEFAULT 0,
    co2_saved           REAL DEFAULT 0,
    transport_choice    TEXT,
    user_id             INTEGER REFERENCES users(id),
    customer_name       TEXT NOT NULL,
    customer_email      TEXT NOT NULL,
    customer_phone      TEXT,
    notes               TEXT,
    status              TEXT DEFAULT 'pending',
    travel_date         DATE,
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS green_points_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL REFERENCES users(id),
    action      TEXT,
    points      INTEGER,
    reference   TEXT,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contact_leads (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT,
    email       TEXT,
    phone       TEXT,
    interest    TEXT,
    message     TEXT,
    source      TEXT,
    contacted   INTEGER DEFAULT 0,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_bookings_email ON bookings(customer_email);
CREATE INDEX IF NOT EXISTS idx_bookings_status ON bookings(status);
CREATE INDEX IF NOT EXISTS idx_gp_log_user ON green_points_log(user_id);
```

---

## HELPER FUNCTIONS (Python)

```python
# db/helpers.py

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '../instance/green_experience.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Trả dict-like rows
    return conn

def generate_booking_code():
    import time
    return f"GE{str(int(time.time()))[-8:]}"

def get_user_level(points: int) -> tuple[str, str]:
    """Returns (level_name, badge_emoji)"""
    levels = [
        (1000, 'Green Legend', '🌍'),
        (600,  'Sustainability Champion', '🏆'),
        (300,  'Eco Warrior', '🌳'),
        (100,  'Green Explorer', '🌿'),
        (0,    'Eco Beginner', '🌱'),
    ]
    for threshold, name, badge in levels:
        if points >= threshold:
            return name, badge
    return 'Eco Beginner', '🌱'

def add_green_points(db, user_id: int, action: str, points: int, reference: str = None):
    """Add points và update user level"""
    db.execute(
        "INSERT INTO green_points_log (user_id, action, points, reference) VALUES (?,?,?,?)",
        (user_id, action, points, reference)
    )
    db.execute(
        "UPDATE users SET green_points = green_points + ? WHERE id = ?",
        (points, user_id)
    )
    # Update level
    user = db.execute("SELECT green_points FROM users WHERE id=?", (user_id,)).fetchone()
    level_name, _ = get_user_level(user['green_points'])
    db.execute("UPDATE users SET level=? WHERE id=?", (level_name, user_id))
    db.commit()
```

---

## STATIC DATA (Python dict — không lưu DB)

```python
# data/static_data.py
# Copy từ mockData.ts, convert sang Python dict

DESTINATIONS = [
    {
        'id': 'lo-lo-chai',
        'name': 'Lô Lô Chải',
        'region': 'Miền Bắc',
        # ... full object từ mockData.ts
    },
    # ...
]

TOURS = [ ... ]      # Full from mockData.ts
HOMESTAYS = [ ... ]
PLASTIC_FREE_SPOTS = [ ... ]
COMMUNITY_ACTIVITIES = [ ... ]
GREEN_POINTS_REWARDS = [ ... ]

# Helper lookups
DESTINATIONS_BY_ID = {d['id']: d for d in DESTINATIONS}
TOURS_BY_ID = {t['id']: t for t in TOURS}
TOURS_BY_DESTINATION = {}
for t in TOURS:
    TOURS_BY_DESTINATION.setdefault(t['destinationId'], []).append(t)
```

---

## ADMIN VIEW (Simple, no framework)

```python
# routes/admin.py
from flask import Blueprint, render_template, session, redirect
from db.helpers import get_db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.before_request
def require_admin():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')
    db = get_db()
    user = db.execute("SELECT is_admin FROM users WHERE id=?", (user_id,)).fetchone()
    if not user or not user['is_admin']:
        return redirect('/')

@admin_bp.route('/bookings')
def bookings():
    db = get_db()
    bookings = db.execute(
        "SELECT * FROM bookings ORDER BY created_at DESC"
    ).fetchall()
    return render_template('admin/bookings.html', bookings=bookings)

@admin_bp.route('/leads')
def leads():
    db = get_db()
    leads = db.execute(
        "SELECT * FROM contact_leads ORDER BY created_at DESC"
    ).fetchall()
    return render_template('admin/leads.html', leads=leads)
```

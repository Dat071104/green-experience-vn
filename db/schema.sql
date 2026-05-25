CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    email         TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    green_points  INTEGER DEFAULT 0,
    level         TEXT DEFAULT 'Eco Beginner',
    role          TEXT DEFAULT 'user',
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
    green_points        INTEGER DEFAULT 0,
    green_points_earned INTEGER DEFAULT 0,
    co2_saved           REAL DEFAULT 0,
    transport_choice    TEXT,
    user_id             INTEGER REFERENCES users(id),
    customer_name       TEXT NOT NULL,
    customer_email      TEXT NOT NULL,
    customer_phone      TEXT,
    notes               TEXT,
    status              TEXT DEFAULT 'pending',
    booking_date        DATE,
    travel_date         DATE,
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS green_points_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL REFERENCES users(id),
    action      TEXT,
    activity_type TEXT,
    description TEXT,
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

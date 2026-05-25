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

import sqlite3
from pathlib import Path

from flask import current_app

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = BASE_DIR / "instance" / "green_experience.db"


def get_db():
    db_path = current_app.config.get("DATABASE", str(DEFAULT_DB_PATH))
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def generate_booking_code():
    import time

    return f"GE{str(int(time.time()))[-8:]}"


def get_user_level(points: int) -> dict:
    levels = [
        (1000, "Green Legend", "Legend"),
        (600, "Sustainability Champion", "Champion"),
        (300, "Eco Warrior", "Warrior"),
        (100, "Green Explorer", "Explorer"),
        (0, "Eco Beginner", "Beginner"),
    ]

    for index, (threshold, name, badge) in enumerate(levels):
        if points >= threshold:
            next_threshold = levels[index - 1][0] if index > 0 else None
            return {
                "name": name,
                "badge": badge,
                "threshold": threshold,
                "next_threshold": next_threshold,
            }

    return {
        "name": "Eco Beginner",
        "badge": "Beginner",
        "threshold": 0,
        "next_threshold": 100,
    }


def add_green_points(db, user_id: int, action: str, points: int, reference: str = None):
    db.execute(
        """
        INSERT INTO green_points_log (user_id, action, description, points, reference)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, action, action, points, reference),
    )
    db.execute(
        "UPDATE users SET green_points = green_points + ? WHERE id = ?",
        (points, user_id),
    )
    user = db.execute("SELECT green_points FROM users WHERE id=?", (user_id,)).fetchone()
    level_info = get_user_level(user["green_points"])
    db.execute("UPDATE users SET level=? WHERE id=?", (level_info["name"], user_id))
    db.commit()

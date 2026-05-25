import sqlite3
import os
from werkzeug.security import generate_password_hash

def init_db():
    instance_dir = 'instance'
    if not os.path.exists(instance_dir):
        os.makedirs(instance_dir)
        
    db_path = os.path.join(instance_dir, 'green_experience.db')
    schema_path = os.path.join('db', 'schema.sql')
    
    # Read schema
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = f.read()
        
    # Execute schema
    conn = sqlite3.connect(db_path)
    conn.executescript(schema)
    
    # Check if we need to add the role column
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'role' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'")
    
    # Add a mock admin user
    hashed = generate_password_hash("admin123")
    try:
        cursor.execute("INSERT INTO users (name, email, password_hash, is_admin, role) VALUES (?, ?, ?, ?, ?)",
                       ("Admin", "admin@greenexperience.vn", hashed, 1, 'staff'))
    except sqlite3.IntegrityError:
        pass # Already exists
        
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()

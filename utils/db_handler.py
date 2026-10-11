import sqlite3
import bcrypt
import os

DB_PATH = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)
    conn.commit()

    # Seed default admin user
    cursor.execute("SELECT id FROM users WHERE username = 'admin'")
    admin_user = cursor.fetchone()
    if not admin_user:
        hashed_admin_pass = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()).decode()
        cursor.execute(
            "INSERT INTO users (username, password, status) VALUES (?, ?, ?)",
            ("admin", hashed_admin_pass, "approved")
        )
        conn.commit()
    conn.close()

# Always ensure database and admin user exist on module load
init_db()

def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password, status FROM users WHERE username = ?",
        (username.strip(),)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        stored_password, status = user
        if status != "approved":
            return "pending"
        if bcrypt.checkpw(password.encode(), stored_password.encode()):
            return "success"
    return "failed"

def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, status) VALUES (?, ?, ?)",
            (username.strip(), hashed_password, "pending")
        )
        conn.commit()
        conn.close()
        return True, "Signup request sent to admin for approval."
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Username already exists."
    except Exception as e:
        conn.close()
        return False, str(e)

def update_password(username, current_password, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(current_password.encode(), user[0].encode()):
        new_hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        cursor.execute(
            "UPDATE users SET password = ? WHERE username = ?",
            (new_hashed, username)
        )
        conn.commit()
        conn.close()
        return True, "Password updated successfully."
    conn.close()
    return False, "Incorrect current password."

def get_pending_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users WHERE status = 'pending'")
    users = cursor.fetchall()
    conn.close()
    return users

def approve_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET status = 'approved' WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return True

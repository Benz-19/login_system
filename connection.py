import sqlite3

conn = sqlite3.connect('your_database.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password VARCHAR NOT NULL
    )
"""
)
conn.commit()


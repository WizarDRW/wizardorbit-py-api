import sqlite3

users = """CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    registered_on TEXT NOT NULL,
    admin BOOLEAN DEFAULT 0,
    public_id TEXT NOT NULL,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL
)"""

def create_table():
    conn=sqlite3.connect('app/main/globalwarning_main.db')
    cur=conn.cursor()
    cur.execute(users)
    conn.commit()
    conn.close()

create_table()
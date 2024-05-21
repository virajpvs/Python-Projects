import sqlite3

conn = sqlite3.connect('user_db.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL 
)
               """)

cursor.execute("""
INSERT INTO users (username, password, name, age, email) VALUES
               ('user1','pass123','mike smith',54, 'mike@gmail.com'),
               ('user2','pass1443','tiron jey',32, 'tiron@gmail.com'),
               ('user3','pass12432','john maxwell',87, 'maxwell@gmail.com')
               """)

conn.commit()
conn.close()






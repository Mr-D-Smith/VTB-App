import sqlite3
import random
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL
               )        
''')

usernames = [
    "alpha",
    "bravo",
    "charlie",
    "delta",
    "echo",
    "foxtrot",
    "golf",
    "hotel",
    "india",
    "juliet",
    "kilo",
    "lima",
    "mike",
    "november",
    "oscar"
]

passwords = [
    "123456",
    "password",
    "qwerty123",
    "letmein123",
    "trustno1",
    "1q2w3e4r",
    "zaq12wsx",
    "killerbee",
    "sunshine22",
    "bluemoon",
    "thunderstorm",
    "monkey77",
    "iloveyou2",
    "dragon2023",
    "football11"
]

username = random.choice(usernames)
password = random.choice(passwords)

cursor.execute('INSERT OR REPLACE INTO users (username,password) VALUES(?,?)',(username,password))

conn.commit()
conn.close()

print("Databse Created.")
print(f"Task: get yourself logged in as {username} {password}")
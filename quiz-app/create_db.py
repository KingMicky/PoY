# create_db.py
import sqlite3

conn = sqlite3.connect('quiz.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        answer TEXT NOT NULL
    )
''')

# Add some sample questions
questions = [
    ('What is the capital of France?', 'Berlin', 'London', 'Paris', 'Madrid', 'Paris'),
    ('What is 2 + 2?', '3', '4', '5', '6', '4'),
    ('What is the capital of Japan?', 'Seoul', 'Tokyo', 'Beijing', 'Bangkok', 'Tokyo')
]

c.executemany('''
    INSERT INTO questions (question, option1, option2, option3, option4, answer)
    VALUES (?, ?, ?, ?, ?, ?)
''', questions)

conn.commit()
conn.close()

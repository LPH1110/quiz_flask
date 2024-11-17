import sqlite3

db_name = 'quiz.sqlite'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    close()

def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do('''CREATE TABLE IF NOT EXISTS quiz(
        id INTEGER PRIMARY KEY,
        name VARCHAR
    )''')

    do('''CREATE TABLE IF NOT EXISTS question(
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS quiz_content(
        id INTEGER PRIMARY KEY,
        quiz_id INTEGER,
        question_id INTEGER,
        FOREIGN KEY (quiz_id) REFERENCES question (id),
        FOREIGN KEY (question_id) REFERENCES question (id)
       )''')

    close()

def add_question():
    questions = [
        ('What is the smallest planet in our solar system?', 'Mercury', 'Venus', 'Earth', 'Mars'),
        ('Who is known as the father of modern physics?', 'Isaac Newton', 'Galileo Galilei', 'Niels Bohr', 'Albert Einstein'),
        ('Which element is represented by the symbol Na?', 'Neon', 'Nickel', 'Nitrogen', 'Sodium'),
        ('What is the main ingredient in traditional Japanese miso soup?', 'Tofu', 'Seaweed', 'Rice', 'Miso paste'),
        ('What is the chemical symbol for gold?', 'Ag', 'Pb', 'Fe', 'Au'),
        ('In which year did the Berlin Wall fall?', '1975', '1991', '1987', '1989')
    ]
    open()
    
    cursor.executemany('''
    INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)
                       ''', questions)
    conn.commit()
    close()

def add_quiz():
    quiz = [
        ('Machine Learning',) ,
        ('Machine Learning 2',),
    ]
    open()

    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quiz)

    conn.commit()
    close()

def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys = on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"

    while input("Add a link (y/n)?") != 'n':
        quiz_id = int(input("quiz id: "))
        question_id = int(input("question id: "))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
    close()

if __name__ == "__main__":
    clear_db()
    create()
    add_question()
    add_quiz()
    add_links()
# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM questions').fetchall()
    conn.close()

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_option = request.form.get(f'question_{question["id"]}')
            if selected_option == question['answer']:
                score += 1
        return redirect(url_for('result', score=score, total=len(questions)))

    return render_template('quiz.html', questions=questions)

@app.route('/result')
def result():
    score = request.args.get('score', type=int)
    total = request.args.get('total', type=int)
    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)

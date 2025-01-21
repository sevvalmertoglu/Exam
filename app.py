from flask import Flask, render_template, request, redirect, url_for, session 
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_db_connection():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        username = request.form['username'] 
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            existing_user = cursor.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            
            if existing_user:
                current_high_score = existing_user["high_score"]
            else:
                cursor.execute('INSERT INTO users (username, high_score) VALUES (?, ?)', (username, 0))
                conn.commit()
                current_high_score = 0
        
        with get_db_connection() as conn:
            questions = conn.execute('SELECT * FROM questions').fetchall()
        
        score = 0
        for question in questions:
            user_answer = request.form.get(f'question-{question["id"]}')
            if user_answer and int(user_answer) == question["correct_option"]:
                score += 1

        total_questions = len(questions)
        percentage = (score / total_questions) * 100
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if score > current_high_score:
                cursor.execute('UPDATE users SET high_score = ? WHERE username = ?', (score, username))
                conn.commit()
        
        session['score'] = score
        session['percentage'] = percentage 
        if 'high_score' not in session or score > session['high_score']:
            session['high_score'] = score
        
        return redirect(url_for('result'))

    with get_db_connection() as conn:
        questions = conn.execute('SELECT * FROM questions').fetchall()
    return render_template('quiz.html', questions=questions)

@app.route('/result')
def result():
    score = session.get('score', 0)
    high_score = session.get('high_score', 0)
    return render_template('result.html', score=score, high_score=high_score)

if __name__ == '__main__':
    app.run(debug=True)

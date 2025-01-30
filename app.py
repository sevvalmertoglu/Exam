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
                user_id = existing_user["id"]
                current_high_score = cursor.execute(
                    'SELECT high_score FROM high_scores WHERE user_id = ?', (user_id,)
                ).fetchone()["high_score"]
            else:
                cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
                user_id = cursor.lastrowid
                cursor.execute('INSERT INTO high_scores (user_id, high_score) VALUES (?, ?)', (user_id, 0))
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
                cursor.execute(
                    'UPDATE high_scores SET high_score = ? WHERE user_id = ?', (score, user_id)
                )
                conn.commit()
                current_high_score = score  
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT MAX(high_score) as max_score FROM high_scores')
            global_high_score = cursor.fetchone()["max_score"]
            global_high_score_percentage = (global_high_score / total_questions) * 100
        
        session['score'] = score
        session['percentage'] = percentage 
        session['high_score'] = current_high_score 
        session['global_high_score'] = global_high_score_percentage  
        
        return redirect(url_for('result'))

    with get_db_connection() as conn:
        questions = conn.execute('SELECT * FROM questions').fetchall()
    return render_template('quiz.html', questions=questions)

@app.route('/result')
def result():
    score = session.get('score', 0)  
    high_score = session.get('high_score', 0)  
    global_high_score = session.get('global_high_score', 0) 

    with get_db_connection() as conn:
        total_questions = conn.execute('SELECT COUNT(*) as count FROM questions').fetchone()["count"]

    score_percentage = (score / total_questions) * 100
    high_score_percentage = (high_score / total_questions) * 100
    global_high_score_percentage = global_high_score  

    return render_template(
        'result.html',
        score=score_percentage,
        high_score=high_score_percentage,
        global_high_score=global_high_score_percentage
    )

if __name__ == '__main__':
    app.run(debug=True)
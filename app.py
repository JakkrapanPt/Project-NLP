from flask import Flask, render_template, request, jsonify
import os
import sqlite3
from app.tokenizers import ThaiTokenizer, EnglishTokenizer
from app.game import GameManager

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        language TEXT NOT NULL,
        mode TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# Initialize tokenizers
thai_tokenizer = ThaiTokenizer()
english_tokenizer = EnglishTokenizer()

# Initialize game manager
game_manager = GameManager(thai_tokenizer, english_tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    language = request.args.get('language', 'thai')
    mode = request.args.get('mode', 'easy')
    return render_template('game.html', language=language, mode=mode)

@app.route('/api/get-challenge', methods=['GET'])
def get_challenge():
    language = request.args.get('language', 'thai')
    mode = request.args.get('mode', 'easy')
    challenge = game_manager.get_challenge(language, mode)
    return jsonify(challenge)

@app.route('/api/check-answer', methods=['POST'])
def check_answer():
    data = request.json
    language = data.get('language', 'thai')
    text = data.get('text', '')
    user_segments = data.get('segments', [])
    
    result = game_manager.check_answer(language, text, user_segments)
    return jsonify(result)

@app.route('/api/save-score', methods=['POST'])
def save_score():
    data = request.json
    player_name = data.get('player_name', 'Anonymous')
    score = data.get('score', 0)
    language = data.get('language', 'thai')
    mode = data.get('mode', 'easy')
    
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO scores (player_name, score, language, mode) VALUES (?, ?, ?, ?)',
        (player_name, score, language, mode)
    )
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

@app.route('/api/high-scores', methods=['GET'])
def high_scores():
    language = request.args.get('language', 'thai')
    mode = request.args.get('mode', 'easy')
    limit = request.args.get('limit', 10, type=int)
    
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT player_name, score, timestamp FROM scores WHERE language = ? AND mode = ? ORDER BY score DESC LIMIT ?',
        (language, mode, limit)
    )
    scores = [{'player': row[0], 'score': row[1], 'date': row[2]} for row in cursor.fetchall()]
    conn.close()
    
    return jsonify(scores)

if __name__ == '__main__':
    # Initialize database
    init_db()
    # Run the app
    app.run(debug=True)
import psycopg2
from flask import Flask, jsonify
import os

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://postgres@db:5432/postgres')
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

@app.route('/characters', methods=['GET'])
def get_characters():
    cursor.execute("SELECT name, class, level, achievements FROM characters ORDER BY achievements DESC")
    rows = cursor.fetchall()
    
    characters = {row[0]: {"class": row[1], "level": row[2], "achievements": row[3]} for row in rows}
    
    return jsonify(characters)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)


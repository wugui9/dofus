import psycopg2
import redis
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Connexion à PostgreSQL pour récupérer les données des personnages
DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://postgres@db:5432/postgres')
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Connexion à Redis pour récupérer le score de popularité
REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
r = redis.StrictRedis.from_url(REDIS_URL)

@app.route('/characters', methods=['GET'])
def get_characters():
    cursor.execute("SELECT name, class, level, achievements FROM characters ORDER BY achievements DESC")
    rows = cursor.fetchall()
    
    # Récupérer les achievements et la popularité de Redis
    characters = {}
    for row in rows:
        name = row[0]
        class_name = row[1]
        level = row[2]
        achievements = row[3]

        # Récupérer le score de popularité depuis Redis (en %)
        popularity = r.get(name)  # On récupère la popularité depuis Redis

        if popularity is None:
            popularity = 0  # Valeur par défaut si aucun score n'est trouvé pour ce personnage
        else:
            popularity = int(popularity)  # Convertir en entier si Redis retourne un score

        characters[name] = {
            "class": class_name, 
            "level": level, 
            "achievements": achievements,
            "popularity": popularity
        }
    
    # Trier les personnages par achievements décroissants
    sorted_characters = {k: v for k, v in sorted(characters.items(), key=lambda item: item[1]['achievements'], reverse=True)}
    
    return jsonify(sorted_characters)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

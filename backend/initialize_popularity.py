import redis
import psycopg2
import os
import random

# Connexion à Redis
REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
r = redis.StrictRedis.from_url(REDIS_URL)

# Connexion à PostgreSQL
DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://postgres@db:5432/postgres')
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Récupérer les personnages depuis PostgreSQL
cursor.execute("SELECT name FROM characters")
rows = cursor.fetchall()

# Assigner un score de popularité aléatoire à chaque personnage (par exemple entre 0 et 100)
for row in rows:
    name = row[0]
    popularity_score = random.randint(0, 100)  # Score de popularité aléatoire
    r.set(name, popularity_score)  # Sauvegarder ce score dans Redis

print("Scores de popularité initialisés dans Redis.")

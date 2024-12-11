from flask import Flask, jsonify, request

app = Flask(__name__)

characters = {
    'VeraShadow': {'class': 'Pandawa', 'level': 60, 'achievements': 200},
    'FiraClaw': {'class': 'Huppermage', 'level': 50, 'achievements': 160},
    'MokaBlaze': {'class': 'Eniripsa', 'level': 60, 'achievements': 150},
    'XyloDust': {'class': 'Ecaflip', 'level': 55, 'achievements': 135},
    'RikoGale': {'class': 'Xelor', 'level': 50, 'achievements': 120},
    'RoboGale': {'class': 'Feca', 'level': 45, 'achievements': 110},
    'LunaFang': {'class': 'Sacrieur', 'level': 38, 'achievements': 95},
    'TikiShade': {'class': 'Iop', 'level': 40, 'achievements': 85},
    'ZaraMoon': {'class': 'Roublard', 'level': 48, 'achievements': 80},
    'VicoStorm': {'class': 'Cra', 'level': 30, 'achievements': 45},
    'TikiClaw': {'class': 'Osamodas', 'level': 25, 'achievements': 30}
}

@app.route('/characters', methods=['GET'])
def get_characters():
    return jsonify(characters)

@app.route('/character/<name>', methods=['GET'])
def get_character(name):
    character = characters.get(name)
    if character:
        return jsonify(character)
    return "Character not found", 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

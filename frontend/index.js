const express = require('express');
const axios = require('axios');
const app = express();
const port = 80;

app.use(express.static('public'));

// Route pour la page d'accueil
app.get('/', async (req, res) => {
  try {
    const characters = await axios.get('http://backend/characters');

    res.send(`
      <html>
        <head>
          <title>Dofus Roster</title>
          <style>
            body { font-family: Arial, sans-serif; }
            h1 { text-align: center; margin-top: 50px; }
            table { width: 80%; margin: 20px auto; border-collapse: collapse; }
            th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
            th { background-color: #f4f4f4; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            tr:hover { background-color: #f1f1f1; }
            .container { width: 90%; margin: 0 auto; }
          </style>
        </head>
        <body>
          <div class="container">
            <h1>Dofus Roster</h1>
            <table>
              <tr>
                <th>Nom</th>
                <th>Classe</th>
                <th>Niveau</th>
                <th>Succès</th>
                <th>Popularité</th> <!-- Nouvelle colonne Popularité -->
              </tr>
              ${Object.keys(characters.data).map(name => `
                <tr>
                  <td>${name}</td>
                  <td>${characters.data[name].class}</td>
                  <td>${characters.data[name].level}</td>
                  <td>${characters.data[name].achievements}</td>
                  <td>${characters.data[name].popularity}%</td> <!-- Affichage du score de popularité -->
                </tr>
              `).join('')}
            </table>
          </div>
        </body>
      </html>
    `);
  } catch (error) {
    res.send("Erreur lors de la récupération des données.");
  }
});

app.listen(port, () => {
  console.log(`Dofus Roster app listening at http://localhost:${port}`);
});

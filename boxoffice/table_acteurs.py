import pandas as pd
import sqlite3

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv('/home/apprenant/Bureau/Box-Office/boxoffice/data/top_acteurs.csv')

# Connexion à la base de données SQLite
conn = sqlite3.connect('base.sqlite3')
cur = conn.cursor()

# Supprimer la table si elle existe déjà
cur.execute('''DROP TABLE IF EXISTS Acteurs''')

# Création de la table Acteurs
cur.execute('''CREATE TABLE Acteurs (
id INTEGER PRIMARY KEY AUTOINCREMENT,
acteur VARCHAR
)''')

# Insertion des données du DataFrame dans la table
for index, row in df.iterrows():
    cast_value = row['acteur']
    cur.execute('''INSERT INTO Acteurs (acteur) VALUES (?)''', (cast_value,))

# Valider les changements dans la base de données
conn.commit()

# Fermer la connexion à la base de données
conn.close()

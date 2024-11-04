import pandas as pd
import sqlite3

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv('/home/apprenant/Bureau/Box-Office/boxoffice/data/data_film.csv')

# Connexion à la base de données SQLite
conn = sqlite3.connect('base.sqlite3')
cur = conn.cursor()

# Création de la table Films
cur.execute('''CREATE TABLE IF NOT EXISTS Film (
id INTEGER PRIMARY KEY,       
title VARCHAR,
release_date DATE,
genre VARCHAR,
duration VARCHAR,
director VARCHAR,
producers VARCHAR,
cast VARCHAR,
nationality VARCHAR ,           
distributor VARCHAR,
box_office_title VARCHAR,
box_office_first_week FLOAT,
press_eval FLOAT,                                               
viewers_eval FLOAT,        
views FLOAT ,                
budget FLOAT
)''')




# Insertion des données du DataFrame dans la table
for index, row in df.iterrows():
 cur.execute('''INSERT INTO Film (
title ,
release_date ,
genre ,
duration ,
director ,
producers ,
cast ,
nationality  ,           
distributor ,
box_office_title ,
box_office_first_week ,
press_eval ,                                               
viewers_eval ,        
views  ,                
budget  )
VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)''',
(row['title'],row['release_date'], row['genre'],row['duration'],row['director'],row['producers'],row['cast'], row['nationality'],row['distributor'],row['box_office_title'], row['box_office_first_week'], row['press_eval'], 
row['viewers_eval'], row['views'],row['budget']))

# Valider les changements dans la base de données
conn.commit()

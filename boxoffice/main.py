import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
import pandas as pd
import os
import numpy as np
from sklearn.base import BaseEstimator



# with open('xgb.pkl','rb') as file:
#     xgb = pickle.load(file)

import joblib
pickle_in = open('data/model.pkl', 'rb') 
model = joblib.load(pickle_in)


app = FastAPI()


# Liste des genres possibles
genres = [
    'action', 'animation', 'arts martiaux', 'aventure', 'biopic', 'bollywood', 'comédie',
    'comédie dramatique', 'comédie musicale', 'divers', 'drame', 'epouvante-horreur', 'erotique',
    'espionnage', 'expérimental', 'famille', 'fantastique', 'guerre', 'historique', 'judiciaire',
    'musical', 'policier', 'péplum', 'romance', 'science fiction', 'sport event', 'thriller', 'western'
]

# Liste des colonnes attendues par le modèle
expected_columns = [
    'nationality', 'duration_minutes', 'season', 'nombre_acteurs_connus', 'distributor_important', 'budget'
] + genres

class PredictionRequest(BaseModel):
    nationality: str
    duration_minutes: int
    season: str
    genre: str
    nombre_acteurs_connus: int
    distributor_important: bool
    budget: float

@app.post("/predict")
def predict(data: PredictionRequest):
    try:
        # Créer un dictionnaire avec des zéros pour tous les genres
        genre_dict = {genre: 0 for genre in genres}
        
        # Mettre à jour le genre correspondant à 1
        if data.genre in genres:
            genre_dict[data.genre] = 1
        
        # Préparer les autres données dans un dictionnaire
        other_features = {
            "nationality": data.nationality,
            "duration_minutes": data.duration_minutes,
            "season": data.season,
            "nombre_acteurs_connus": data.nombre_acteurs_connus,
            "distributor_important": data.distributor_important,
            "budget" : data.budget
        }
        
        # Combiner les deux dictionnaires
        features_dict = {**other_features, **genre_dict}
        
        # Convertir en DataFrame
        features_df = pd.DataFrame([features_dict])
        
        # Faire la prédiction en utilisant le pipeline
        prediction = model.predict(features_df)
        print(prediction)
        
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=float(e))




# @app.post("/predict2")
# def predict2(data: PredictionRequest):
#     df=pd.DataFrame(columns = ['nationality', 'duration_minutes', 'season', 'action', 'animation',
#        'arts martiaux', 'aventure', 'biopic', 'bollywood', 'comédie',
#        'comédie dramatique', 'comédie musicale', 'divers', 'drame',
#        'epouvante-horreur', 'erotique', 'espionnage', 'expérimental',
#        'famille', 'fantastique', 'guerre', 'historique', 'judiciaire',
#        'musical', 'policier', 'péplum', 'romance', 'science fiction',
#        'sport event', 'thriller', 'western', 'stars_producers_director',
#        'nombre_acteurs_connus', 'distributor_important'])
#     genre = data.genre


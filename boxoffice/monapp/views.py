from django.shortcuts import render, redirect
from .forms import LoginForm, PredictForm
from django.contrib.auth import authenticate, login, logout
from .run_spider import run_allocine_spider
from .run_scrapy import run_scrapy
from main import predict, PredictionRequest
import requests
import csv
import os 
import json
import datetime
import joblib
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


logger = logging.getLogger(__name__)

def homepage(request):
    return render(request, 'monapp/home.html')

def home_login(request):
    form = LoginForm()
    print("value :", request.user.is_authenticated)
    if request.method == 'POST':
        logger.info(f"{datetime.datetime.now()}l'utilisateur soumets le formulaire de connexion")
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                print(request.user.is_authenticated)
                logger.info(f"{datetime.datetime.now()}L'utilisateur s'est connecté")
                return redirect('homepage')
            else:
                message = 'Identifiants invalides'
                logger.info(f"{datetime.datetime.now()}l'utilisateur a rentré de mauvais identifiants")
                print(message)
                return render(request, 'monapp/login.html', context={'form': form, 'message': message})

    return render(request, 'monapp/login.html', context={'form': form})



def a_propos(request):
    logger.info(f"{datetime.datetime.now()}l'utilisateur est sur la page a propos")
    return render(request, 'a_propos.html')

def logout_user(request):
    logger.info(f"{datetime.datetime.now()}l'utilisateur s'est déconnecté")
    logout(request)
    return redirect('homepage')

# def scrape_and_predict(request):
#     # Exécuter le spider Scrapy en tant que sous-processus
#     run_scrapy()

#     # Charger les résultats du scrapping
#     films_csv_path = os.path.join(os.path.dirname(__file__), '..', 'allocine_scraper', 'films.csv')
#     films = []

#     with open(films_csv_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             films.append(row)

#     # Simulation de prédiction (à remplacer par votre modèle de prédiction)
#     predictions = []
#     for film in films:
#         prediction = {
#             'film': film,
#             'prediction': 100000,  # Remplacez par votre prédiction réelle
#             'box_office_divided': 1000  # Remplacez par votre calcul réel
#         }
#         predictions.append(prediction)

#     context = {
#         'predictions': predictions,
#     }

#     return render(request, 'scrape_and_predict.html', context)

# # Charger le modèle de machine learning (assurez-vous d'avoir un modèle enregistré)
# model_path = os.path.join(os.path.dirname(__file__), 'your_model.pkl')
# model = joblib.load(model_path)


def predict_boxoffice(request):
    form = PredictForm()
    if request.method == 'POST':
        logger.info(f"{datetime.datetime.now()}l'utilisateur soumets les information du film")
        form = PredictForm(request.POST or None)
        print(form.data)
        nationality = form.data['nationality']
        duration_minutes = form.data['duration']
        season = form.data['season']
        genre = form.data['genre']
        nombre_acteurs_connus = form.data['num_known_actors']
        distributor_important = form.data['distributor'] == 'on'
        budget = form.data['budget']

        # Préparer les données pour l'API
        data = {
            'nationality': nationality,
            'duration_minutes': duration_minutes,
            'season': season,
            'genre': genre,
            'nombre_acteurs_connus': nombre_acteurs_connus,
            'distributor_important': distributor_important,
            'budget' : budget
        }

        # Sélection des clés d'intérêt pour la prédiction
        liste_cle = ['nationality', 'duration_minutes', 'season', 'genre', 'nombre_acteurs_connus', 'distributor_important', 'budget']
        data_cleaned = {cle: data[cle] for cle in liste_cle}
        print(data)


        try:
            # Envoi de la requête POST à l'API de prédiction
            response = requests.post("http://127.0.0.1:8000/predict", json=data_cleaned)

            if response.status_code == 200:
                prediction = response.json().get('prediction', 'No prediction returned')
            else:
                prediction = "Error in prediction API call"
        except requests.exceptions.RequestException as e:
            prediction = f"API request failed: {e}"

        return render(request, 'predict_boxoffice.html', {'form': form, 'prediction': prediction})

    return render(request, 'predict_boxoffice.html', {'form': form})

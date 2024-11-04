import pandas as pd
from django.utils import timezone
from monapp.models import Film, ActeursFilm, Boxoffice

# Lire le fichier CSV dans un DataFrame
csv_file_path = 'boxoffice/data/data_film.csv'
df = pd.read_csv(csv_file_path)

# Itérer sur le DataFrame et créer les instances de modèles
for index, row in df.iterrows():
    # Créer ou obtenir l'instance Film
    film, created = Film.objects.get_or_create(
        titre=row['titre'],
        distributeur=row['distributeur'],
        defaults={
            'date': pd.to_datetime(row['date']).date() if not pd.isnull(row['date']) else timezone.now().date(),
            'genre': row['genre'] if not pd.isnull(row['genre']) else 'Unknown',
            'box_office_first_week': row['box_office_first_week'],
            'press_eval': row['press_eval'],
            'viewers_eval': row['viewers_eval'],
            'views': row['views'],
            'budget': row['budget']
        }
    )

    # Créer les instances ActeursFilm associées
    acteurs = row['acteurs'].split(',')  # Supposons que les acteurs soient séparés par des virgules dans le CSV
    for acteur in acteurs:
        ActeursFilm.objects.get_or_create(film=film, acteur=acteur.strip())

    # Créer les instances Boxoffice associées
    boxoffice_revenues = row['boxoffice_revenues'].split(',')  # Supposons que les revenus soient séparés par des virgules dans le CSV
    for revenue in boxoffice_revenues:
        Boxoffice.objects.create(
            film=film,
            revenue=float(revenue.strip()),
            date=timezone.now().date()  # Remplacer par la date appropriée si disponible
        )

print("Les données CSV ont été chargées dans la base de données Django.")
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model




class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


class PredictForm(forms.Form):
    NATIONALITY_CHOICES = [
        # Ajoutez ici les options de nationalité si nécessaire
    ]

    SEASON_CHOICES = [
        ('Hiver', 'Hiver'),
        ('Printemps', 'Printemps'),
        ('Été', 'Été'),
        ('Automne', 'Automne'),
    ]

    GENRE_CHOICES = [
        ('Drame', 'Drame'),
        ('Comédie', 'Comédie'),
        ('Thriller', 'Thriller'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Comédie dramatique', 'Comédie dramatique'),
        ('Aventure', 'Aventure'),
        ('Animation', 'Animation'),
        ('Fantastique', 'Fantastique'),
        ('Policier', 'Policier'),
        ('Famille', 'Famille'),
        ('Épouvante-horreur', 'Épouvante-horreur'),
        ('Science fiction', 'Science fiction'),
        ('Biopic', 'Biopic'),
        ('Historique', 'Historique'),
        ('Musical', 'Musical'),
        ('Guerre', 'Guerre'),
        ('Comédie musicale', 'Comédie musicale'),
        ('Espionnage', 'Espionnage'),
        ('Western', 'Western'),
        ('Arts Martiaux', 'Arts Martiaux'),
        ('Judiciaire', 'Judiciaire'),
        ('Érotique', 'Érotique'),
        ('Bollywood', 'Bollywood'),
        ('Péplum', 'Péplum'),
        ('Expérimental', 'Expérimental'),
        ('Sport event', 'Sport event'),
        ('Divers', 'Divers'),
    ]

    nationality = forms.CharField(
        label="Nationalité du Film",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input', 'id': 'nationality', 'required': True})
    )

    duration = forms.IntegerField(
        label="Durée (en minutes)",
        widget=forms.NumberInput(attrs={'class': 'input', 'id': 'duration', 'required': True})
    )

    season = forms.ChoiceField(
        label="Saison",
        choices=SEASON_CHOICES,
        widget=forms.Select(attrs={'class': 'select', 'id': 'season', 'required': True})
    )

    genre = forms.ChoiceField(
        label="Genre du Film",
        choices=GENRE_CHOICES,
        widget=forms.Select(attrs={'class': 'select', 'id': 'genre', 'required': True})
    )

    num_known_actors = forms.IntegerField(
        label="Nombre d'acteurs connus",
        widget=forms.NumberInput(attrs={'class': 'input', 'id': 'num_known_actors', 'required': True})
    )

    distributor = forms.CharField(
        label="Distributeur connu",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input', 'id': 'distributor', 'required': True})
    )
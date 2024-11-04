from django.db import models
from django.utils import timezone

class Film(models.Model):
    titre = models.CharField(max_length=500)
    distributeur = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now)
    genre = models.CharField(max_length=100, default='Unknown')
    box_office_first_week = models.IntegerField()
    press_eval = models.FloatField()
    viewers_eval = models.FloatField()
    views = models.FloatField()
    budget = models.FloatField()

    class Meta:
        db_table = 'films'

    def __str__(self):
        return self.titre

class ActeursFilm(models.Model):
    film = models.ForeignKey(Film, related_name='acteurs', on_delete=models.CASCADE)
    acteur = models.CharField(max_length=500)

    class Meta:
        db_table = 'acteurs_films'

class Boxoffice(models.Model):
    film = models.ForeignKey(Film, related_name='boxoffice', on_delete=models.CASCADE)
    box_office_title = models.CharField(max_length=255)
    box_office_first_week = models.IntegerField(null = True)

    class Meta:
        db_table = 'boxoffice'

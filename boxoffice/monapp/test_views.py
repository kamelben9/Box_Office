import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user(db):
    user = User.objects.create_user(username='testuser', password='password')
    return user

@pytest.mark.django_db
def test_homepage(client):
    response = client.get(reverse('homepage'))
    assert response.status_code == 200
    assert '<title>Accueil</title>' in response.content.decode('utf-8')  # Ajuste ceci pour correspondre à ton template

@pytest.mark.django_db
def test_login_get(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200
    assert 'form' in response.context
    assert 'message' not in response.context

@pytest.mark.django_db
def test_login_post_invalid(client):
    response = client.post(reverse('login'), {'username': 'wrong', 'password': 'wrong'})
    assert response.status_code == 200
    assert 'message' in response.context
    assert response.context['message'] == 'Identifiants invalides'

@pytest.mark.django_db
def test_login_post_valid(client, user):
    response = client.post(reverse('login'), {'username': user.username, 'password': 'password'})
    assert response.status_code == 302  # Redirection après succès de connexion
    assert response.url == reverse('homepage')

@pytest.mark.django_db
def test_a_propos(client):
    response = client.get(reverse('a_propos'))
    assert response.status_code == 200
    assert '<title>A Propos</title>' in response.content.decode('utf-8')  # Ajuste ceci pour correspondre à ton template

@pytest.mark.django_db
def test_predict_boxoffice_get(client):
    response = client.get(reverse('predict_boxoffice'))
    assert response.status_code == 200
    assert 'form' in response.context

@pytest.mark.django_db
def test_predict_boxoffice_post(client):
    data = {
        'nationality': 'FR',
        'duration': '120',
        'season': 'summer',
        'genre': 'comedy',
        'num_known_actors': '3',
        'distributor': 'on'
    }
    response = client.post(reverse('predict_boxoffice'), data)
    assert response.status_code == 200
    assert 'prediction' in response.context
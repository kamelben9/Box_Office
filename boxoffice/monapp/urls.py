from django.contrib import admin
from django.urls import path, include
from monapp import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.home_login,name='login'),
    # path('box_office/',views.box_office,name='box_office'),
    # path('start-scraping/', views.scraping_view, name='scraping_view'),
    # path('start-scraping-bo/', views.scraping_boxoffice_view, name='scraping_boxoffice_view'),
    path('a_propos/', views.a_propos, name='a_propos'),
    # path('scrape_and_predict/', views.scrape_and_predict, name='scrape_and_predict'),
    path('predict_boxoffice/', views.predict_boxoffice, name='predict_boxoffice'),
    # path('signup/', views.SignupPage.as_view(), name='signup'),
    # path('home_user/',views.home_user,name='home_user')
]


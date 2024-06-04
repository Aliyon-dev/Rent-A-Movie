from django.urls import path
from .views import home, login, customers, movies

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('customers', customers, name="customers"), 
    path('movies', movies, name="movies")
]

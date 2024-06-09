from django.urls import path
from .views import home, login, customers, movies, add_customer, test, add_movie, get_genres

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('customers', customers, name="customers"), 
    path('movies', movies, name="movies"),
    path('add_customer', add_customer, name="add_customer"),
    path('add_movie', add_movie, name="add_movie"),
    path('get_genres', get_genres, name="get_genres"),
    path('modal', test)
]

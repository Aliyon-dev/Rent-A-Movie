from django.urls import path
from .views import home, login, customers, movies, add_customer, test

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('customers', customers, name="customers"), 
    path('movies', movies, name="movies"),
    path('add_customer', add_customer, name="add_customer"),
    path('modal', test)
]

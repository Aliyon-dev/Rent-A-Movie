from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('customers', customers, name="customers"), 
    path('movies', movies , name="movies"),
    path('add-customer', add_customer, name="add_customer"),
    path('add-movie', add_movie, name="add_movie"),
    path('get_genres', get_genres, name="get_genres"),
    path('get-movie', get_movies, name="get_movies"),
    path('get-movie/<int:key>', get_movie, name="get-movie"),
    path('update-movie/<int:key>', update_movie, name="update-movie"),
    path('delete-movie/<int:key>', delete_movie, name="delete-movie"),
    path('get-customers', get_customers, name="get_customers"),
    path('customer/<int:customer_id>/', get_customerDetails, name='customer_detail'), 
    path('customer/<int:customer_id>/update/', update_customer, name='update_customer'),
    path('customer/<int:customer_id>/delete/', delete_customer, name='delete_customer'),
    path('get-city/<str:key>', get_city, name="get_city")
    
]

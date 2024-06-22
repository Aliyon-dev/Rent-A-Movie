from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('base', base, name="base"),
    path('login', user_login, name="login"),
    path('logout', user_logout, name="logout"),
    path('customers', customers, name="customers"), 
    path('movies', movies , name="movies"),
    path('rentals', transactions, name="rentals"),
    path('add-customer', add_customer, name="add_customer"),
    path('add-movie', add_movie, name="add_movie"),
    path('get-genres', get_genres, name="get_genres"),
    path('get-movie', get_movies, name="get_movies"),
    path('get-movie/<int:key>', get_movie, name="get-movie"),
    path('update-movie/<int:key>', update_movie, name="update-movie"),
    path('delete-movie/<int:key>', delete_movie, name="delete-movie"),
    path('get-customers', get_customers, name="get_customers"),
    path('customer/<int:customer_id>/', get_customerDetails, name='customer_detail'), 
    path('update-customer/<int:id>', update_customer, name='update_customer'),
    path('delete-customer/<int:id>', delete_customer, name='delete_customer'),
    path('get-city/<str:key>', get_city, name="get_city"),
    path('metrics', home_metrics, name="home_metrics"),
    path('get-rentals',get_rentals, name="get_rentals"),
    path('add-rental', add_rental, name="add_rental"),
    path('get-top-genres', get_top_genres, name="get_top_genres"),
    path('get-customer-metrics/<int:id>', get_customer_metrics, name="get_customer_metrics")
    
    #path('post-movie', post_movie, name="post_movie"),
    
]

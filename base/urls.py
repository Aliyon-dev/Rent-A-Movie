from django.urls import path
from .views import delete_customer, get_customerDetails, home, login, customers, movies, add_customer, test, add_movie, get_genres, crud_movie, update_customer

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('customers', customers, name="customers"), 
    path('movies', movies, name="movies"),
    path('add_customer', add_customer, name="add_customer"),
    path('add_movie', add_movie, name="add_movie"),
    path('get_genres', get_genres, name="get_genres"),
    path('get-movie/<int:key>', crud_movie, name="get-movie"),
    path('get-movie/<str:key>', crud_movie, name="get-movie"),
    path('modal', test),
    path('customer/<int:customer_id>/', get_customerDetails, name='customer_detail'), 
    path('customer/<int:customer_id>/update/', update_customer, name='update_customer'),
    path('customer/<int:customer_id>/delete/', delete_customer, name='delete_customer'),
]

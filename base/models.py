from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myUser(User):
    name = models.CharField(max_length=6)
    age = models.IntegerField()



class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_type = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    release_year = models.DateField(auto_now=False, auto_now_add=False)
    language = models.CharField(max_length=50)
    
    
class Actor(models.Model):
    Fname = models.CharField( max_length=50)
    Lname = models.CharField(max_length=50)
    
class Movie_Actor(models.Model):
    ActorID = models.ForeignKey(Actor, on_delete=models.CASCADE)
    MovieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('ActorID', 'MovieID'),)
    
class Rental(models.Model):
    rental_date = models.DateField(auto_now=False)
    rental_expiry = models.DateField(auto_now=False)
    rental_cost = models.IntegerField()
    rental_cost_total = models.IntegerField()


class Movie_rental(models.Model):
    MovieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    RentalID = models.ForeignKey(Rental, on_delete=models.CASCADE)
    class meta:
        unique_together = (('MovieID', 'RentalID'),)
    
class Customer(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    phone =  models.IntegerField()
    zip_code = models.IntegerField()
    street_address = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)
    
    
    
class Transaction(models.Model):
    transaction_date = models.DateField( auto_now=False, auto_now_add=False)
    Price = models.IntegerField()
    Tax = models.IntegerField()
    
class Customer_Transaction(models.Model):
    TransactionID = models.ForeignKey(Transaction,  on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
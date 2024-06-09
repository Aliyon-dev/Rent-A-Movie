from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myUser(User):
    name = models.CharField(max_length=6)
    age = models.IntegerField()



class Genre(models.Model):
    genre =  models.CharField(max_length=50)

    def __str__(self):
        return self.genre
    


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    img_url = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title


class Movie_genre(models.Model):
    genreID = models.ForeignKey(Genre,  on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
class Actor(models.Model):
    Fname = models.CharField( max_length=50)
    Lname = models.CharField(max_length=50)
    
class Movie_Actor(models.Model):
    ActorID = models.ForeignKey(Actor, on_delete=models.CASCADE)
    MovieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('ActorID', 'MovieID'),)
        
    def __str__(self):
        return self.ActorID
    
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
    id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    phone =  models.IntegerField()
    zip_code = models.IntegerField()
    #street_address = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        self.name = f'{self.Fname} {self.Lname}'   
        return self.name 
    
    
class Transaction(models.Model):
    transaction_date = models.DateField( auto_now=False, auto_now_add=False)
    Price = models.IntegerField()
    Tax = models.IntegerField()
    
class Customer_Transaction(models.Model):
    TransactionID = models.ForeignKey(Transaction,  on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
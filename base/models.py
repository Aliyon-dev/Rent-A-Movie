from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myUser(User):
    name = models.CharField(max_length=6)
    age = models.IntegerField()


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, default="English")
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class MovieActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('actor', 'movie'),)

    def __str__(self):
        return f'{self.actor} in {self.movie}'

class Rental(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rental_date = models.DateField(auto_now=False)
    rental_expiry = models.DateField(auto_now=False)
    rental_tax = models.FloatField()
    rental_cost_total = models.FloatField()

    def __str__(self):
        return f'Rental {self.id} for {self.customer}'


class ZipCode(models.Model):
    zip_code = models.CharField(max_length=10, primary_key=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.zip_code

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.PROTECT)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, default="email")
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.customer} on {self.date}'
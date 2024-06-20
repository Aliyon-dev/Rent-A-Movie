import os
import django
import random
from faker import Faker
from datetime import timedelta
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rentAmovie.settings')
django.setup()

from base.models import Genre, Movie, Actor, MovieActor, Rental, MovieRental, ZipCode, Customer, Message

fake = Faker()

# Generate Genres
def create_genres(num=10):
    genres = []
    for _ in range(num):
        genre = Genre(name=fake.word())
        genre.save()
        genres.append(genre)
    return genres

# Generate Movies
def create_movies(genres, num=50):
    movies = []
    for _ in range(num):
        movie = Movie(
            title=fake.sentence(nb_words=3),
            genre=random.choice(genres),
            language=fake.language_name(),
            price=round(random.uniform(5.0, 30.0), 2)
        )
        movie.save()
        movies.append(movie)
    return movies

# Generate Actors
def create_actors(num=50):
    actors = []
    for _ in range(num):
        actor = Actor(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )
        actor.save()
        actors.append(actor)
    return actors

# Create MovieActor relationships
def create_movie_actors(actors, movies):
    for _ in range(len(actors) * 2):  # Assuming each actor can be in multiple movies
        movie_actor = MovieActor(
            actor=random.choice(actors),
            movie=random.choice(movies)
        )
        movie_actor.save()

# Generate ZipCodes
def create_zipcodes(num=20):
    zipcodes = []
    for _ in range(num):
        zipcode = ZipCode(
            zip_code=fake.zipcode(),
            city=fake.city(),
            state=fake.state()
        )
        zipcode.save()
        zipcodes.append(zipcode)
    return zipcodes

# Generate Customers
def create_customers(zipcodes, num=50):
    customers = []
    for _ in range(num):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            zip_code=random.choice(zipcodes),
            phone=fake.phone_number(),
            email=fake.email(),
            street_address=fake.street_address()
        )
        customer.save()
        customers.append(customer)
    return customers

# Generate Rentals
def create_rentals(customers, movies, num=100):
    rentals = []
    for _ in range(num):
        rental_date = timezone.now() - timedelta(days=random.randint(1, 100))
        rental = Rental(
            customer=random.choice(customers),
            rental_date=rental_date,
            rental_expiry=rental_date + timedelta(days=random.randint(1, 30)),
            rental_cost=round(random.uniform(5.0, 15.0), 2),
            rental_tax=round(random.uniform(1.0, 5.0), 2),
            rental_cost_total=round(random.uniform(6.0, 20.0), 2)
        )
        rental.save()
        rentals.append(rental)
    return rentals

# Create MovieRental relationships
def create_movie_rentals(movies, rentals):
    for _ in range(len(movies) * 2):  # Assuming each movie can be rented multiple times
        movie_rental = MovieRental(
            movie=random.choice(movies),
            rental=random.choice(rentals)
        )
        movie_rental.save()

# Generate Messages
def create_messages(customers, num=100):
    for _ in range(num):
        message = Message(
            customer=random.choice(customers),
            message=fake.text(max_nb_chars=200),
            date=fake.date_this_year(),
            time=fake.time()
        )
        message.save()

if __name__ == '__main__':
    print("Generating fake data...")
    genres = create_genres()
    movies = create_movies(genres)
    actors = create_actors()
    create_movie_actors(actors, movies)
    zipcodes = create_zipcodes()
    customers = create_customers(zipcodes)
    rentals = create_rentals(customers, movies)
    create_movie_rentals(movies, rentals)
    create_messages(customers)
    print("Fake data generation complete.")

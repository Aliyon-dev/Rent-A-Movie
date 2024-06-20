import os
import django
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rentAmovie.settings')
django.setup()

from base.models import Genre, Movie

fake = Faker()

# Predefined list of logical movie genres
GENRES = [
    "Action", "Adventure", "Animation", "Comedy", "Crime",
    "Documentary", "Drama", "Family", "Fantasy", "History",
    "Horror", "Music", "Mystery", "Romance", "Science Fiction",
    "TV Movie", "Thriller", "War", "Western"
]

# Function to create genres
def create_genres(genres):
    genre_objects = []
    for genre_name in genres:
        genre, created = Genre.objects.get_or_create(name=genre_name)
        genre_objects.append(genre)
        if created:
            print(f'Created genre: {genre.name}')
        else:
            print(f'Genre already exists: {genre.name}')
    return genre_objects

# Function to create movies
def create_movies(genres, num=50):
    for _ in range(num):
        movie = Movie(
            title=fake.sentence(nb_words=3),
            genre=random.choice(genres),
            language=fake.language_name(),
            price=round(random.uniform(5.0, 30.0), 2)
        )
        movie.save()
        print(f'Created movie: {movie.title} with genre {movie.genre.name}')

if __name__ == '__main__':
    print("Generating logical movie genres...")
    genres = create_genres(GENRES)
    print("Genre data generation complete.")

    print("Generating random movies...")
    create_movies(genres, num=50)  # Change the number if you need more or fewer movies
    print("Movie data generation complete.")

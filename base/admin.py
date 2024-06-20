from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(myUser)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(MovieActor)
#admin.site.register(MovieRental)
admin.site.register(Rental)
admin.site.register(Customer)
#admin.site.register(Movie_genre)
admin.site.register(Genre)
admin.site.register(ZipCode)
admin.site.register(Message)


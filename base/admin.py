from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(myUser)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Movie_Actor)
admin.site.register(Movie_rental)
admin.site.register(Rental)
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Customer_Transaction)
#admin.site.register(Movie_genre)
admin.site.register(Genre)
admin.site.register(ZipCode)


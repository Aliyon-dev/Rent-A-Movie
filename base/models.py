from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myUser(User):
    name = models.CharField(max_length=6)
    age = models.IntegerField()
    
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function to render the home page
def home(request):
    return render(request, 'base.html')



#function to handle login from the user
def login(request):
    return HttpResponse("Login")
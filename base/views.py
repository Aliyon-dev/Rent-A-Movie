from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from  .models import Customer
# Create your views here.

# function to render the home page
def home(request):
    return render(request, 'index.html')



#function to handle login from the user
def login(request):
    if request.method =="POST":
        email = request.POST.get ("username")
        password = request.POST.get ("password")
        user =authenticate (request, username=email,password=password)
        if user is not None:
            login(request, user)
            # redirect to a home page 
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Unable to login'})
            # return an invalid error message 
    return render(request, 'login.html')

def customers(request):
    return render(request, 'customers.html')

def movies(request):
    return render(request, 'movies.html')




def add_customer(request):
    if request.method=='POST':
        form =Customer(request.POST)
        if form.is_valid():
            #getting user details
            Fname=form.cleand
      
        print(request.POST)
    return render(request, 'add_customers.html')


def test(request):
    return render(request, 'base.html')


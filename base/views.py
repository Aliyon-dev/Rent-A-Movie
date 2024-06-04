from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function to render the home page
def home(request):
    return render(request, 'index.html')



#function to handle login from the user
def login(request):
    email = request.POST.get("username")
    password = request.POST.get("password")
    
    #### authenticate
    
    #### if valid, login
        #### once logged take user to home page
        
    
    #### Return an error and ask user to try again
    
    print(f'the {email} and {password}')
    
    return render(request, 'login.html')


def customers(request):
    return render(request, 'customers.html')

def movies(request):
    return render(request, 'movies.html')
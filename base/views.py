from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.db import connection
from .models import *
from rest_framework.decorators import api_view
from .serializers import genre_serializer
from django.http import JsonResponse
from .models import Customer

# Create your views here.

# function to render the home page
def home(request):
    return render(request, 'index.html')


# function to handle login from the user
def login(request):
    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
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
    context_dict = {}
    with connection.cursor() as cursor:
        cursor.execute(
            """     SELECT id, title, type, price
                    FROM base_movie
            """
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    return render(request, 'movies.html')


def add_customer(request):
    if request.method == 'POST':
        Fname = request.POST.get("Fname")
        Lname = request.POST.get("Lname")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zipcode")
        phone_number = request.POST.get("phone")
        email = request.POST.get("email")

        #customer = Customer()
        #customer.Fname = Fname
        #customer.Lname = Lname
        #customer.city = city
        #customer.zip_code = int(zip_code)
        #customer.phone = phone_number
        #customer.state = state
        #customer.save()
        #customers = Customer.objects.all()
        print(f'{Fname}, {Lname}, {city}, {state}, {zip_code}, {phone_number}, {email}')
        with connection.cursor() as cursor:
           cursor.execute(
               "INSERT INTO base_customer(Fname, Lname, city, state, zip_code, phone, email) VALUES (%s, %s, %s,%s, %s, %s,%s)",
               [Fname,Lname,city,state, zip_code,phone_number,email ]
           )
        return redirect('customers')
        return render(request, 'add_customers.html',{'customers': customers})
    customers = Customer.objects.all()
    return render(request, 'add_customers.html',{'customers':customers})        




def get_customers(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM base_customer LIMIT 200")
        customers = cursor.fetchall()

    return render(request, 'add_customers.html', {'customers': customers})


def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        type = request.POST.get("type")
        price = request.POST.get("price")
        url = request.POST.get("thumbnail")
        print(f"Received title: {title}, type: {type}, price: {price} img: {url}")
        #with connection.cursor() as cursor:
        #    cursor.execute(
        #        "INSERT INTO base_movie (title, type, price) VALUES (%s, %s, %s)",
        #        [title, type, price]
        #    )
        #return redirect('movies')
    return render(request, 'movies.html')


def test(request):
    return render(request, 'base.html')


@api_view(['GET'])
def get_genres(request):
    if request.method == "GET":
        try:
            genre = Genre.objects.all()
            serializer = genre_serializer(genre, many=True)
            return JsonResponse(serializer.data, safe=False)

        except Exception as e:
            print(e)
            return JsonResponse({"error": "error"})

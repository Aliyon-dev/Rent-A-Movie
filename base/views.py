from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.db import connection
from .models import *
from rest_framework.decorators import api_view
from .serializers import genre_serializer, movie_serializer
from django.http import JsonResponse
from .models import Customer
from rest_framework.response import Response

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
        movie_list = {"movies": []}
        
        for row in rows:
            movie = {
                "id": row[0],
                "title": row[1],
                "type": row[2],
                "price": row[3]
            }
            movie_list["movies"].append(movie)
        #print(movie_list)
    return render(request, 'movies.html', context=movie_list)


@api_view(['GET', 'DELETE', 'PUT'])
def crud_movie(request, key):
    
    ### getting a specific movie ###
    if request.method =='GET':
        try:
            movie = Movie.objects.get(pk=key)
            print(movie)
            serializer = movie_serializer(movie)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return JsonResponse({"error": "error"})
        
    ### deleting a movie ###     
    elif request.method=='DELETE':
        try:
            movie = Movie.objects.get(pk=key)
            movie.delete()
            return JsonResponse({"message": f'Movie with title "{movie.title}" has been deleted successfully'})
        except Exception as e:
            error = str(e)
            return JsonResponse({"error": error})
        
    ### editing a movie ###   
    elif request.method == 'PUT':
        try:
            movie = Movie.objects.get(pk=key)
            serializer = movie_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "succesfully edited",})
            else:
                return JsonResponse({"message": "Unable to edit the movie"})       
        except Exception as e:
            return JsonResponse({"message": str(e)})

def add_customer(request):

    if request.method == 'POST':
        
        Fname = request.POST.get("Fname")
        Lname = request.POST.get("Lname")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zipcode")
        phone_number = request.POST.get("phone")

        customer = Customer()
        customer.Fname = Fname
        customer.Lname = Lname
        customer.city = city
        customer.zip_code = int(zip_code)
        customer.phone = phone_number
        customer.state = state
        customer.save()
        # customers = Customer.objects.all()
        with connection.cursor() as cursor:
           cursor.execute(
               "INSERT INTO base_customer(id, Fname, Lname, city, state, zip_code, phone) VALUES (%s, %s, %s,%s, %s, %s,%s)",
               [id, Fname, Lname,city, state, zip_code,phone_number ]
           )
        return redirect('customer')

        return render(request, 'add_customers.html',{'customers': customers})
    
    customers = Customer.objects.all()

    return render(request, 'add_customers.html',{'customrs':customers})        

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
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO base_movie (title, type, price) VALUES (%s, %s, %s)",
                [title, type, price]
            )
        return redirect('movies')
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


def get_customerDetails (request, customer_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT* FROM base_customer WHERE id =%s", [customer_id])
        customer =cursor.fetchone()

    if customer is None:
        return render(request, 'custome_detail.html', {'error': 'Customer not found'})
    
    return render(request, 'customer_detail.html',{'customer' : customer})


def update_customer (request):
    if request.method =='POST':
        Fname = request.POST.get("Fname")
        Lname = request.POST.get("Lname")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zipcode")
        phone_number = request.POST.get("phone")


        # #ensure zip code is a valid integer
        # try:
        #     zip_code =(int zip_code)
        # except ValueError:
        #     #Handle the error, maybe return an error message
        #     return render (request, 'add customers.html', {'error':'Zip code must be a 5- digit number.'})
        
        with connection.cursor()as cursor:
            cursor. excute (
                "UPDATE base_customer SET Fname = %s, Lname = %s, city = %s, state = %s, zip_code = %s, phone_number = %s WHERE id = %s",
                [Fname, Lname, city, state, zip_code, phone_number, id]

            )
        return redirect ('customer')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM base_customer WHERE id = %s", [id])
        customer = cursor.fetchone()

    if customer is None:
        return render (request, 'update_customer.html', {'erroe': 'Customer'})
    return render(request, 'Update_customer.html', {'customer': customer})


def delete_customer (request, customer_id):
    with connection.cursor() as cursor:
        cursor.excute ("DELETE FROM base_customer WHERE id=%s", [customer_id])

    return redirect ('customer')    
        


    
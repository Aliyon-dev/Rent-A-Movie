from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.db import connection
from .models import *
from rest_framework.decorators import api_view
from .serializers import genre_serializer, movie_serializer, customer_serializers, zipcode_serializers, rental_serializers
from django.http import JsonResponse
from .models import Customer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import pytz

# Create your views here.

# function to render the home page
def home(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


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
    return render(request, 'movies.html')




@api_view(['GET'])
def get_movies(request):
    if request.method == 'GET':
        try:
            movies = Movie.objects.all()
            serializer = movie_serializer(movies, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as error:
            return JsonResponse({"Message": str(error)})
    #context_dict = {}
    #with connection.cursor() as cursor:
    #    cursor.execute(
    #        """     SELECT id, title, type, price
    #                FROM base_movie
    #        """
    #    )
    #    rows = cursor.fetchall()
    #    movie_list = {"movies": []}
    #    
    #    for row in rows:
    #        movie = {
    #            "id": row[0],
    #            "title": row[1],
    #            "type": row[2],
    #            "price": row[3]
    #        }
    #        movie_list["movies"].append(movie)
    #    #print(movie_list)
    return render(request, 'movies.html')

@api_view(['PUT'])
def update_movie(request, key):
    try:
        if request.method == 'PUT':
            movie = Movie.objects.get(pk=key)
            serializer = movie_serializer(instance=movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"Successfully updated": serializer.data})
            else:
                return JsonResponse({"message": "unable to update movie"})

    except Exception as error:
        return JsonResponse({"Message": str(error)})



@api_view(['DELETE'])
def delete_movie(request, key):
    try:
        if request.method == 'DELETE':
            movie = Movie.objects.get(pk=key)
            movie.delete()
            return JsonResponse({"Message":"Movie has deleted successfully"})
        else:
            return JsonResponse({"Wrong Method, expected 'DELETE' "})
    except Exception as error:
        return JsonResponse({"Message": str(error)})
            
    

#@api_view(['GET'])
def get_movie(request, key):
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
    return render(request, 'movies.html')


#@api_view(['POST'])
#def post_movie(request):
#    if request.method == 'POST':
#        title = request.POST.get("title")
#        genre = request.POST.get("genre")
#        price = request.POST.get("price")
#        language = request.POST.get("language")
#        
#        try:
#            movie = Movie.objects.create(
#                title=title,
#                genre = Genre.objects.get(name=genre),
#                price= price,
#                language=language,
#            )
#            return JsonResponse({"success": "Movie added"})
#
#        except Exception as error:
#            return JsonResponse({"message": str(error)})
            



@api_view(['POST'])
def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        type = request.POST.get("genre")
        price = request.POST.get("price")
        language = request.POST.get("language")
        try:
            movie =  Movie.objects.create(
            title=title,
            genre = Genre.objects.get(name=type),
            language=language,
            price = price
            )
            return JsonResponse({"message": f'{title} added successfully'})
        
        except Exception as error:
            return JsonResponse({"error": str(error)})

@api_view(['POST'])
def add_customer(request):
    if request.method == 'POST':
        Fname = request.POST.get("fname")
        Lname = request.POST.get("lname")
        city = request.POST.get("city")
        email = request.POST.get("email")
        zip_code = request.POST.get("zipcode")
        phone_number = request.POST.get("phone")
        
        print(f'{Fname} {Lname} {city} {email} {zip_code} {phone_number}')
        
        customer = Customer.objects.create(
            first_name=Fname,
            last_name=Lname,
            city=city,
            phone=phone_number,
            zip_code=ZipCode.objects.get(zip_code=zip_code),
            email=email,
        )
        
        return JsonResponse({"success": Fname})
        
        
        #with connection.cursor() as cursor:
        #   cursor.execute(
        #       "INSERT INTO base_customer(id, Fname, Lname, city, state, zip_code, phone) VALUES (%s, %s, %s,%s, %s, %s,%s)",
        #       [id, Fname, Lname,city, state, zip_code,phone_number ]
        #   )
        #return redirect('customer')


@api_view(['GET'])
def get_customers(request):
    try:
        if request.method == 'GET':
           # with connection.cursor() as cursor:
           #     cursor.execute("SELECT * FROM base_customer LIMIT 200")
           #     
           # customers = cursor.fetchall()
           movie = Customer.objects.all()
           serializer = customer_serializers(movie, many=True)
           return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        return JsonResponse({"Error": str(e)})





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
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT* FROM base_customer WHERE id =%s", [customer_id])
    #    customer =cursor.fetchone()
    
    customer = Customer.objects.get(pk=customer_id)
    serializer = customer_serializers(customer)
    return JsonResponse(serializer.data)


@api_view(['POST'])
def update_customer (request, id):
    if request.method =='POST':
        city = request.POST.get("city")
        email = request.POST.get("email")
        zip_code = request.POST.get("zipcode")
        phone_number = request.POST.get("phone")
        customer = Customer.objects.get(pk=id)
        print("fuck", city)
        
        print(f'{city} {zip_code} {phone_number} {email}')
        if city != None:
            customer.city = city
        if zip_code != None:
            customer.zip_code = ZipCode.objects.get(zip_code=zip_code)
        if phone_number != None:
            customer.phone != email
        if email != None:
            customer.email = email
            
        customer.save()
        
        return JsonResponse({"success": "success"})

        

        #with connection.cursor()as cursor:
        #    cursor. execute (
        #        "UPDATE base_customer SET city = %s, state = %s, zip_code = %s, phone_number = %s, email = %s, WHERE id = %s",
        #        [city, state, zip_code, phone_number, email, id]
#
        #    )
        return JsonResponse({"message": "success"})

@api_view(['DELETE'])
def delete_customer (request, id):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM base_customer WHERE id=%s", [id])
        return JsonResponse({"success": "success"})
    return JsonResponse({"error": str(e)})



@api_view(['GET'])
def get_city(request, key):
    if request.method=='GET':
        try:
            city = ZipCode.objects.get(pk=str(key))
            serializer = zipcode_serializers(city)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": "invalid zipcode"}, status=status.HTTP_404_NOT_FOUND)

        
    

def transactions(request):
    return render(request, 'rentals.html')



@api_view(['GET'])
def get_metrics(request):
    pass
    
    
    
@api_view(['GET'])
def home_metrics(request):
    customers = Customer.objects.all().count()
    movies = Movie.objects.all().count()
    rental = Rental.objects.all()
    rentals = rental.count()
    
    profit = 0
    for items in rental:
        profit = profit + int(items.rental_cost_total)
        
    return JsonResponse({"customers": customers,
                         "movies": movies,
                         "rentals": rentals,
                         "profits": profit})

@api_view(['GET'])
def get_rentals(request):
    if request.method == 'GET':
        rentals = Rental.objects.select_related('movie', 'customer').all()
        for rental in rentals:
            print(rental.movie.title)
        serializer = rental_serializers(rentals, many=True)
        return JsonResponse(serializer.data, safe=False)



@api_view(['POST'])
def add_rental(request):
    if request.method == 'POST':
        customer = request.POST.get("customer")
        movie   = request.POST.get("movie")
        rental_date = request.POST.get("rental_date")
        rental_expiry = request.POST.get("rental_expiry")
        #tax_rate = request.POST.get("tax_rate")
        db_movie =  Movie.objects.get(title=movie)
        cost = float(db_movie.price)
        total_cost = cost + (cost*(float(15)/100))
        first_name = customer.split(" ")[0]
        last_name= customer.split(" ")[1]
        
        name = customer.split(" ")
        print(name)
        
        print(last_name)
        
        rental_date_ = datetime.strptime(rental_date, '%Y-%m-%dT%H:%M')
        rental_expiry_ = datetime.strptime(rental_expiry, '%Y-%m-%dT%H:%M')
        
    
        rental = Rental.objects.create(
            customer=Customer.objects.get(first_name=first_name, last_name=last_name),
            movie = db_movie,
            rental_date = rental_date_,
            rental_expiry = rental_expiry_,
            rental_tax = 15,
            rental_cost_total=total_cost              
        )
        return JsonResponse({"Message": "Success"})
        
    
    
@api_view(['GET'])
def get_top_genres(request):
    rentals = Rental.objects.select_related('movie').all()
    genre = []
    for rental in rentals:
        movie = Movie.objects.select_related('genre').get(title=rental.movie.title)
        genre_ = (movie.genre.name)
        genre.append(genre_)
    
    print(genre)   
    counts = {item: genre.count(item) for item in set(genre)}
    print(counts)
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)[:6])
    return JsonResponse(sorted_counts)
    
        
@api_view(['GET'])
def get_customer_metrics(request, id):
    customer = Customer.objects.get(pk=id)
    name = customer.first_name + " "+ customer.last_name
    rentals = Rental.objects.select_related('customer', 'movie').filter(customer=id)
    movies_rented = rentals.count()
    amount_spent = 0
    active_rentals = 0
    movies = []
    i = 0

    for rental in rentals:
        amount_spent = amount_spent + rental.rental_cost_total
        date = rental.rental_expiry
        now =  datetime.today().date()
        if date > now:
            active_rentals = active_rentals + 1
    for rental in rentals:
        print(rental)
        movies.append([i, [rental.movie.title, rental.rental_date]])
        i = i+1
    dict = {key: value for key, value in movies}
    
    
    print(dict)
    
    return JsonResponse({"movies_rented": movies_rented,
                         "amount_spent": amount_spent,
                         "active_rentals": active_rentals,
                         "movies": dict})
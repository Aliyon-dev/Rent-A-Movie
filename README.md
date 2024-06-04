# Rent-A-Movie Database Project

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://travis-ci.org/username/repo.svg?branch=main)](https://travis-ci.org/username/repo)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

The Rent-A-Movie Database Project is designed to manage and enhance the operations of a movie rental store. The system allows the store to keep track of their customers, the movies they rent, and related transactions. This project aims to improve the store's ability to market and provide enhanced service to its customers.

## Features

- Search for customers by last name or phone number
- Automatically retrieve city and state information from a zip code when entering new customers
- Track movies rented by customers, including rental dates, and spending details
- Generate personalized letters for customers
- Search for movies by name, type, or actor

## Technologies

- Django 3.2
- Python 3.8
- MySQL
- Bootstrap 4

## Installation

Follow these steps to set up the Rent-A-Movie Database Project locally.

### Prerequisites

Ensure you have the following installed on your local machine:
- Python 3.8
- pip
- virtualenv
- MySQL

### Steps

1. Clone the repository
   ```sh
   git clone https://github.com/Aliyon-dev/Rent-A-Movie.git


## Features to implement 

## Home Page View (home):
 Create a Django view function to render the home page.
 Create a template (e.g., home.html) for the home page content.
 Define a URL pattern to map the home page view.
 
## Customer List View (customer_list):
 Create a Django view function to list all customers.
 Retrieve customer data from the database using a Django model.
 Create a template (e.g., customer_list.html) to display the list of customers.
 Define a URL pattern to map the customer list view.

 
## Movie List View (movie_list):
 Create a Django view function to list all movies.
 Retrieve movie data from the database using a Django model.
 Create a template (e.g., movie_list.html) to display the list of movies.
 Define a URL pattern to map the movie list view.
 
## Customer Detail View (customer_detail):
 Create a Django view function to display detailed information about a customer.
 Retrieve customer data based on an identifier (e.g., customer ID) from the database.
 Create a template (e.g., customer_detail.html) to display the customer details.
 Define a URL pattern to map the customer detail view with a dynamic URL parameter.

 
## Movie Detail View (movie_detail):
 Create a Django view function to display detailed information about a movie.
 Retrieve movie data based on an identifier (e.g., movie ID) from the database.
 Create a template (e.g., movie_detail.html) to display the movie details.
 Define a URL pattern to map the movie detail view with a dynamic URL parameter.
 
## Add New Customer View (add_customer):
 Create a Django view function to render a form for adding a new customer.
 Process the form data submitted by the user to add a new customer to the database.
 Validate the form data to ensure it meets required criteria.
 Create a template (e.g., add_customer.html) to display the add customer form.
 Define a URL pattern to map the add customer view.
 
## Add New Movie View (add_movie):
 Create a Django view function to render a form for adding a new movie.
 Process the form data submitted by the user to add a new movie to the database.
 Validate the form data to ensure it meets required criteria.
 Create a template (e.g., add_movie.html) to display the add movie form.
 Define a URL pattern to map the add movie view.
 
## Login View:
 Create a Django view function to handle user login.
 Render a login form for users to input their credentials.
 Validate the form data and authenticate the user.
 Redirect the user to the home page upon successful login.
 Display appropriate error messages for failed login attempts.
 Define a URL pattern to map the login view.

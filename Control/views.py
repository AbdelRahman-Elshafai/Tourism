from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect

from .models import Admin

from Countries.models import Countries, Cities , Comments , Experience , Locations
# Create your views here.


def display_dash_board(request):

    return render(request , 'home.html')


def display_car_rental(request):

    return render(request , 'table.html')


def display_car_reservation(request):

    return render(request , 'table.html')

def display_cities(request):

    return render(request , 'table.html')

def display_comments(request):

    return render(request , 'table.html')

def display_countries(request):

    countries = Countries.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Countries._meta.get_fields()][1:]


    context = {"name": "Countries", "all": countries, "field_names": field_names}


    return render(request , 'table.html' , context)

def display_experience(request):

    return render(request , 'table.html')

def display_locations(request):

    return render(request , 'table.html')

def display_users(request):

    return render(request , 'table.html')

def display_car_rental(request):

    return render(request , 'table.html')


def create_car_reservation(request):

    return render(request , 'home.html')

def create_cities(request):

    return render(request , 'home.html')

def create_comments(request):

    return render(request , 'home.html')

def create_countries(request):

    return render(request , 'home.html')

def create_experience(request):

    return render(request , 'home.html')

def create_locations(request):

    return render(request , 'home.html')

def create_users(request):

    return render(request , 'home.html')

def create_car_rental(request):

    return render(request , 'home.html')
from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect

from .models import Admin

from Countries.models import Countries, Cities , Comments , Experience , Locations

from Car_Rental.models import Car_Rental , Car_Reservation

from Profile.models import User

# Create your views here.


def display_dash_board(request):

    return render(request , 'home.html')


def display_car_rental(request):

    rental = Car_Rental.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Car_Rental._meta.get_fields()][1:]


    context = {"name": "Car Rental", "all": rental, "field_names": field_names}


    return render(request , 'table.html' , context)


def display_car_reservation(request):

    reservation = Car_Reservation.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Car_Reservation._meta.get_fields()][1:]


    context = {"name": "Car Reservation", "all": reservation, "field_names": field_names}


    return render(request , 'table.html' , context)

def display_cities(request):

    cities = Cities.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Cities._meta.get_fields()][2:]

    context = {"name": "Cities", "all": cities, "field_names": field_names}


    return render(request , 'table.html' , context)

def display_comments(request):

    comments = Comments.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Comments._meta.get_fields()][1:]


    context = {"name": "Comments", "all": comments, "field_names": field_names}


    return render(request , 'table.html' , context)

def display_countries(request):

    countries = Countries.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Countries._meta.get_fields()][1:]


    context = {"name": "Countries", "all": countries, "field_names": field_names}


    return render(request , 'table.html' , context)

def display_experience(request):

    experience = Experience.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Experience._meta.get_fields()][1:]


    context = {"name": "Experience", "all": experience, "field_names": field_names}


    return render(request , 'table.html' , context)

def display_locations(request):

    locations = Locations.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Locations._meta.get_fields()][1:]


    context = {"name": "Locations", "all": locations, "field_names": field_names}


    return render(request , 'table.html' , context)

def display_users(request):

    users = User.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in User._meta.get_fields()][1:]


    context = {"name": "Users", "all": users, "field_names": field_names}


    return render(request , 'table.html' , context)



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
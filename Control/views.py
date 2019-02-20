from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect

from .models import Admin

from .forms import CountriesForm, CitiesForm, LocationsForm, UserForm, HotelForm

from Countries.models import Countries, Cities , Comments , Experience , Locations

from Car_Rental.models import  Car_Reservation

from Profile.models import UserProfile

from hotel.models import Hotel , HotelReservationRequest

# Create your views here.


def display_dash_board(request):

    return render(request , 'home.html')


def display_cities(request):

    cities = Cities.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Cities._meta.get_fields()][2:]

    context = {"name": "Cities", "all": cities, "field_names": field_names}


    return render(request , 'table.html' , context)



def display_countries(request):

    countries = Countries.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Countries._meta.get_fields()][1:]


    context = {"name": "Countries", "all": countries, "field_names": field_names}


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

    field_names = [field.name for field in User._meta.get_fields()][4:]


    context = {"name": "Users", "all": users, "field_names": field_names}


    return render(request , 'table.html' , context)


def display_hotels(request):

    hotels = Hotel.objects.all()

    # get all the field names of the model

    field_names = [field.name for field in Hotel._meta.get_fields()][2:]

    context = {"name": "Hotels", "all": hotels, "field_names": field_names}


    return render(request , 'table.html' , context)







def create_cities(request):

    form = CitiesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"cities_form" : form})



def create_countries(request):

    form = CountriesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"countries_form" : form})



def create_locations(request):

    form = LocationsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"locations_form" : form})

def create_users(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"users_form" : form})

def create_hotels(request):

    form = HotelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"hotel_form" : form})



def edit_countries(request , country_name):


    country = Countries.objects.get(country_name = country_name)

    form = CountriesForm(request.POST or None , instance= country)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"countries_form" : form})





def edit_cities(request , city_name):
    city = Cities.objects.get(city_name = city_name)
    form = CitiesForm(request.POST or None , instance= city)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"cities_form" : form})



def edit_locations(request , location_name):

    location = Locations.objects.get(location_name = location_name)

    form = LocationsForm(request.POST or None , instance=location)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"locations_form" : form})



def edit_hotels(request , hotel_name):

    hotels = Hotel.objects.get(hotel_name = hotel_name)

    form = HotelForm(request.POST or None , instance=hotels)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Control/panel")
    else:
        return render(request , 'form.html' , {"hotel_form" : form})



def delete_countries(request , country_ID):

    country = Countries.objects.get(country_ID = eval(country_ID))

    country.delete()


    return HttpResponseRedirect("/Control/panel")



def delete_cities(request , city_ID):

    city = Cities.objects.get(city_ID = eval(city_ID))

    city.delete()


    return HttpResponseRedirect("/Control/panel")



def delete_locations(request , location_ID):

    location = Locations.objects.get(location_ID = eval(location_ID))

    location.delete()


    return HttpResponseRedirect("/Control/panel")



def delete_hotels(request , hotel_id):

    hotel = Hotel.objects.get(hotel_id = eval(hotel_id))

    hotel.delete()


    return HttpResponseRedirect("/Control/panel")
from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect

from .models import Admin

from .forms import CountriesForm , CitiesForm , CommentsForm , ExperienceForm , LocationsForm , UserForm , RentalForm , ReservationForm

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

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Control/panel")
    else:

        form = ReservationForm()

        context = {"reservation_form": form}

        return render(request, 'form.html', context)

def create_cities(request):

    if request.method == "POST":
        form = CitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Control/panel")
    else:

        form = CitiesForm()

        context = {"cities_form": form}

        return render(request, 'form.html', context)

def create_comments(request):

    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Control/panel")
    else:

        form = CommentsForm()

        context = {"comments_form": form}

        return render(request, 'form.html', context)

def create_countries(request):

    if request.method == "POST":
        form = CountriesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Control/panel")
    else:

        form = CountriesForm()

        context = {"countries_form": form}

        return render(request, 'form.html', context)


def create_experience(request):

    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Control/panel")
    else:

        form = ExperienceForm()

        context = {"experience_form": form}

        return render(request, 'form.html', context)

def create_locations(request):

    if request.method == "POST":
        form = LocationsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Control/panel")
    else:

        form = LocationsForm()

        context = {"locations_form": form}

        return render(request, 'form.html', context)

def create_users(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Control/panel")
    else:

        form = UserForm()

        context = {"users_form": form}

        return render(request, 'form.html', context)

def create_car_rental(request):

    if request.method == "POST":
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Control/panel")
    else:

        form = RentalForm()

        context = {"rental_form": form}

        return render(request, 'form.html', context)
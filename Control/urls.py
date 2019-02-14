"""iti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin

from django.contrib.auth import urls

from Control import views

urlpatterns = [
    url(r'^panel/$', views.display_dash_board),
    url(r'^panel/CarRental$', views.display_car_rental),
    url(r'^panel/CarReservation$', views.display_car_reservation),
    url(r'^panel/Cities$', views.display_cities),
    url(r'^panel/Comments$', views.display_comments),
    url(r'^panel/Countries$', views.display_countries),
    url(r'^panel/Experience$', views.display_experience),
    url(r'^panel/Locations$', views.display_locations),
    url(r'^panel/Users$', views.display_users),
    url(r'^panel/ReservationForm$', views.create_car_reservation),
    url(r'^panel/CitiesForm$', views.create_cities),
    url(r'^panel/CommentsForm$', views.create_comments),
    url(r'^panel/CountriesForm$', views.create_countries),
    url(r'^panel/ExperienceForm$', views.create_experience),
    url(r'^panel/LocationsForm$', views.create_locations),
    url(r'^panel/UsersForm$', views.create_users),
    url(r'^panel/RentalForm$', views.create_car_rental),

]
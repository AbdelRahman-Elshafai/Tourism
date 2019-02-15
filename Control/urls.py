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


    url(r'^panel/Countries/edit/(?P<country_name>[-\w\s]+)/$', views.edit_countries),
    # url(r'^panel/CarRental/edit/(?P<country_name>[-\w|\W]+)/$', views.edit_car_rental),
    # url(r'^panel/CarReservation/edit/(?P<country_name>[-\w|\W]+)/$', views.edit_car_reservation),
    url(r'^panel/Cities/edit/(?P<city_name>[-\w\s]+)/$', views.edit_cities),
    # url(r'^panel/Comments/edit/(?P<comment_ID>[-\w|\W]+)/$', views.edit_comments),
    # url(r'^panel/Experience/edit/(?P<country_name>[-\w|\W]+)/$', views.edit_experience),
    url(r'^panel/Locations/edit/(?P<location_name>[-\w\s]+)/$', views.edit_locations),
    # url(r'^panel/Users/edit/(?P<user_name>[-\w|\W]+)/$', views.edit_users),


    url(r'^panel/Countries/delete/(?P<country_ID>[0-9]+)/$', views.delete_countries),
    # url(r'^panel/CarRental/delete/(?P<country_name>[-\w|\W]+)/$', views.edit_car_rental),
    # url(r'^panel/CarReservation/delete/(?P<country_name>[-\w|\W]+)/$', views.edit_car_reservation),
    url(r'^panel/Cities/delete/(?P<city_ID>[0-9]+)/$', views.delete_cities),
    # url(r'^panel/Comments/delete/(?P<comment_ID>[-\w|\W]+)/$', views.edit_comments),
    # url(r'^panel/Experience/delete/(?P<country_name>[-\w|\W]+)/$', views.edit_experience),
    url(r'^panel/Locations/delete/(?P<location_ID>[0-9]+)/$', views.delete_locations),
    # url(r'^panel/Users/delete/(?P<user_name>[-\w|\W]+)/$', views.edit_users),

]
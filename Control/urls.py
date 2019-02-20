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
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/$', views.display_dash_board , name='home'),

    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Cities$', views.display_cities),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Countries$', views.display_countries),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Locations$', views.display_locations),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Users$', views.display_users),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Hotels$', views.display_hotels),


    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/CitiesForm$', views.create_cities),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/CountriesForm$', views.create_countries),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/LocationsForm$', views.create_locations),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/UsersForm$', views.create_users),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/HotelsForm$', views.create_hotels),

    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Countries/edit/(?P<country_name>[-\w\s]+)/$', views.edit_countries),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Cities/edit/(?P<city_name>[-\w\s]+)/$', views.edit_cities),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Locations/edit/(?P<location_name>[-\w\s]+)/$', views.edit_locations),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Hotels/edit/(?P<hotel_name>[-\w\s]+)/$', views.edit_hotels),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Users/edit/(?P<username>[-\w|\W]+)/$', views.edit_users),


    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Countries/delete/(?P<country_ID>[0-9]+)/$', views.delete_countries),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Cities/delete/(?P<city_ID>[0-9]+)/$', views.delete_cities),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Locations/delete/(?P<location_ID>[0-9]+)/$', views.delete_locations),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Hotels/delete/(?P<hotel_id>[0-9]+)/$', views.delete_hotels),
    url(r'^[A-Za-z\- / A-Za-z\-]+/panel/Users/delete/(?P<id>[-\w|\W]+)/$', views.delete_users),

]
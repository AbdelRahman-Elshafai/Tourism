from django.contrib import admin
from .models import *

# Register your models here.

class customCountries(admin.ModelAdmin):
    fieldsets = (['Countries_info',{'fields':['country_ID','country_name','local_name','latitude','longitude','rate']}],)
    list_display = ('country_ID','country_name','local_name','latitude','longitude','rate')

class customCities(admin.ModelAdmin):
    fieldsets = (['Cities_info', {'fields': ['city_ID', 'city_name', 'local_name', 'country_ID', 'latitude','longitude','description' , 'rate']}],)
    list_display = ('city_ID', 'city_name', 'local_name', 'country_ID', 'latitude','longitude','description' , 'rate')



admin.site.register(Countries,customCountries)
admin.site.register(Cities,customCities)
admin.site.register(Locations)
admin.site.register(Experience)
admin.site.register(Comments)



from django.contrib import admin
from .models import *
from Profile.models import Users

# Register your models here.

class customCountries(admin.ModelAdmin):
    fieldsets = (['Countries_info',{'fields':['country_ID','country_name','local_name','latitude','longitude','rate']}],)
    list_display = ('country_ID','country_name','local_name','latitude','longitude','rate')

class customCities(admin.ModelAdmin):
    fieldsets = (['Cities_info', {'fields': ['city_ID', 'city_name', 'local_name', 'country_ID', 'latitude','longitude','description' , 'rate']}],)
    list_display = ('city_ID', 'city_name', 'local_name', 'country_ID', 'latitude','longitude','description' , 'rate')

class customLocations(admin.ModelAdmin):
    fieldsets = (['Locations_info',{'fields':['location_ID','location_name','city_ID','latitude','longitude','description']}],)
    list_display = ('location_ID','location_name','city_ID','latitude','longitude','description')

class customExperience(admin.ModelAdmin):
    fieldsets = (['Experience_info', {'fields': ['exper_ID', 'user_ID', 'city_ID', 'date', 'description']}],)
    list_display = ('exper_ID', 'user_ID', 'city_ID', 'date', 'description')


class customComments(admin.ModelAdmin):
    fieldsets = (['Comments_info',{'fields':['comment_ID','user_ID','exper_ID','date','description']}],)
    list_display = ('comment_ID','user_ID','exper_ID','date','description')



admin.site.register(Countries,customCountries)
admin.site.register(Cities,customCities)
admin.site.register(Locations,customLocations)
admin.site.register(Experience,customExperience)
admin.site.register(Comments,customComments)



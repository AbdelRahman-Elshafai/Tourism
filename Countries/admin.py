from django.contrib import admin
from .models import *
from Profile.models import Users

# Register your models here.

class customCountries(admin.ModelAdmin):
    fieldsets = (
        ['Countries_info',{'fields':['country_name','local_name','latitude','longitude','rate']}],
    )

class customCities(admin.ModelAdmin):
    fieldsets = (['Cities_info', {'fields': ['city_name', 'local_name', 'country_ID', 'latitude','longitude','description' , 'rate']}],)

class customLocations(admin.ModelAdmin):
    fieldsets = (['Locations_info',{'fields':['location_name','city_ID','latitude','longitude','description']}],)

class customExperience(admin.ModelAdmin):
    fieldsets = (['Experience_info', {'fields': [ 'user_ID', 'city_ID', 'date', 'description']}],)


class customComments(admin.ModelAdmin):
    fieldsets = (['Comments_info',{'fields':['user_ID','exper_ID','date','description']}],)



admin.site.register(Countries,customCountries)
admin.site.register(Cities,customCities)
admin.site.register(Locations,customLocations)
admin.site.register(Experience,customExperience)
admin.site.register(Comments,customComments)



from django.contrib import admin
from .models import *

class CustomResevation(admin.ModelAdmin):
    fieldset = (
        ['Car_Reservation', {'fields': ['reservation_id', 'rental_id', 'user_id']}],
    )

class CustomRental(admin.ModelAdmin):
    fieldsets = (
        ['Car_Rental', {'fields': ['Car_Rental_id', 'Car_Rental_Name']}],
    )


# Register your models here.
admin.site.register(Car_Reservation, CustomResevation)
admin.site.register(Car_Rental, CustomRental)
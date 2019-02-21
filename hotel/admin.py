from django.contrib import admin

from .models import Hotel ,HotelReservationRequest

# Register your models here.


class customHotel(admin.ModelAdmin):
    fieldsets = (
        ['Hotel_Info',{'fields':['hotel_name','city_id']}],
    )



class customHotelReservation(admin.ModelAdmin):
    fieldsets = (
        ['Hotel_Reservation',{'fields':['from_date','to_date','no_of_adults' , 'hotel_id' , 'user_id']}],
    )





admin.site.register(Hotel,customHotel)
admin.site.register(HotelReservationRequest,customHotelReservation)

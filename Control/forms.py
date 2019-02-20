from django import forms

from Countries.models import Countries , Comments , Cities , Locations , Experience

from Profile.models import Users

from hotel.models import Hotel

from Car_Rental.models import  Car_Reservation

from .models import Admin


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('admin_username','admin_password')




class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = ('country_name' , 'local_name' , 'latitude' , 'longitude' , 'rate')


class CitiesForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ('city_name' , 'local_name' , 'country_ID' , 'latitude' , 'longitude' , 'description' , 'rate')

class LocationsForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ('location_name' , 'city_ID' , 'latitude' , 'longitude' , 'description')


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        # fields = ('username' , 'first_name' , 'last_name' , 'user_password' , 'user_email' , 'blk_flg')


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('hotel_name' , 'hotel_id' , 'city_id')




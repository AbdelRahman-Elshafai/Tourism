from django import forms

from Countries.models import Countries , Comments , Cities , Locations , Experience

from Profile.models import User

from Car_Rental.models import Car_Rental , Car_Reservation

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


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('user_ID' , 'city_ID', 'date', 'description')


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('user_ID' , 'exper_ID' , 'date' , 'description')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'user_password' , 'user_email' , 'blk_flg')


class RentalForm(forms.ModelForm):
    class Meta:
        model = Car_Rental
        fields = ('car_rental_name' , 'location_ID')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Car_Reservation
        fields = ('rental_id' , 'user_id')
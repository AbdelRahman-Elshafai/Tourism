from django import forms
from django.forms import TextInput

from .models import HotelReservationRequest
from .models import Hotel


# form class
# class reservationForm(forms.ModelForm):
#
#     class Meta:
#         model = HotelReservationRequest
#         fields = ('hotel_id', 'user_id', 'from_date', 'to_date', 'no_of_adults',)
#
#         def __init__(self, *args, **kwargs):
#             super(reservationForm, self).__init__(*args, **kwargs)
#             self.fields['hotel_id'].queryset = Hotel.objects.filter(city_id = '1')
# 	    ## number 1 in last line is merely a test.


class choice_field(forms.ChoiceField):
    def valid_value(self, value):
        return True



class ReserveForm(forms.Form):

    #make the choice field with intial value to pick up his location
    hotels = choice_field( widget=forms.Select() , required=False )

    #make the pick up date of form
    from_date = forms.DateTimeField(widget=forms.DateTimeField() , required=True)

    #make the drop off date of form
    to_date = forms.DateTimeField(widget=forms.DateTimeField() , required=True)

    no_adult_choices = [(1 , '1') , (2 , '2') , (3 , '3') , (4 , '4')]
    #the number of adults
    no_adults = choice_field( choices=no_adult_choices , widget=forms.Select() , required=False)

    def __init__(self, *args, **kwargs):
        super(ReserveForm, self).__init__(*args, **kwargs)

        #override the id and class to match the css
        self.fields['from_date'].widget = TextInput(attrs={
            'id': 'datepicker',
            'class': 'dates form-control',
            'placeholder': 'Date & time'})

        #override the id and class to match the css
        self.fields['to_date'].widget = TextInput(attrs={
            'id': 'datepicker2',
            'class': 'dates form-control',
            'placeholder': 'Date & time'})
from django import forms
from django.forms import fields_for_model, SelectDateWidget, TextInput
from Countries.models import Countries


# TOPIC_CHOICES = (('general', 'General enquiry'), ('bug', 'Bug report'), ('suggestion', 'Suggestion'),)
# country_list = Countries.objects.all()
#
# class ContactForm (forms.Form):
#     topic = forms.ChoiceField(choices=country_list)
#     message = forms.CharField(widget=forms.Textarea())
#     sender = forms.EmailField(required=False)
#



class RentalForm(forms.Form):

    #make the choice field with intial value to pick up his location
    location = forms.ChoiceField( widget=forms.Select() , required=False )

    #make the pick up date of form
    pick = forms.DateTimeField(widget=forms.DateTimeField() , required=True)

    #make the drop off date of form
    drop = forms.DateTimeField(widget=forms.DateTimeField() , required=True)

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)

        #override the id and class to match the css
        self.fields['pick'].widget = TextInput(attrs={
            'id': 'datepicker',
            'class': 'dates form-control',
            'placeholder': 'Date & time'})

        #override the id and class to match the css
        self.fields['drop'].widget = TextInput(attrs={
            'id': 'datepicker2',
            'class': 'dates form-control',
            'placeholder': 'Date & time'})
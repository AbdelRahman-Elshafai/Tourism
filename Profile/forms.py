from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required Field.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required Field.')
    user_email = forms.EmailField(max_length=254, required= True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'user_email', 'password1', 'password2', )
from django import forms
from .models import User


class RegisterationForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('user_name' , 'first_name', 'last_name', 'user_password' , 'user_email',)
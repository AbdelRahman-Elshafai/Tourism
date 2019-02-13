from django import forms
from .models import User


class RegisterationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_name' , 'first_name', 'last_name', 'user_passwd' , 'user_email',)
from django import forms
from django.contrib.auth.forms import UserCreationForm

from Profile.models import UserProfile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# def validate_pass(value):
#     if not any(char.isdigit() for char in value):
#         raise ValidationError(
#             _('The password must contain numbers'),
#             params={'value': value},
#         )
#     elif len(value) < 8:
#         raise ValidationError(
#             _('The password must be at least 8 characters'),
#             params={'value': value},
#         )



class SignUpForm(UserCreationForm):
    username  = forms.CharField(max_length=200 , required=True)
    first_name= forms.CharField(max_length=200 , required=True)
    last_name = forms.CharField(max_length=200 , required=True)
    password1 = forms.CharField(max_length=200 , widget=forms.PasswordInput , label="Password")
    password2 = forms.CharField(max_length=200 , widget=forms.PasswordInput , label="Confirm Password")
    email     = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = UserProfile
        fields = ('username' , 'first_name', 'last_name', 'password1' , 'password2' ,'email' )


    def addUser (self, commit = True):
        user = super(SignUpForm,self).save(commit = False)
        user.email      = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']

        if commit == True:
            self.save()
        return user


# class LogInForm(forms.ModelForm):
#     user_password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'user_password' )



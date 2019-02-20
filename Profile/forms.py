from django import forms
from django.contrib.auth.forms import UserCreationForm

from Profile.models import UserProfile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _




class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                 max_length=32, help_text='First name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                                max_length=32, help_text='Last name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64,
                             help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta:
        model = UserProfile
        fields = ('username' , 'first_name', 'last_name', 'password1' , 'password2' ,'email' )


    # def addUser (self, commit = True):
    #     user = super(SignUpForm,self).save(commit = False)
    #     user.email      = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name  = self.cleaned_data['last_name']
    #
    #     if commit == True:
    #         self.save()
    #     return user



from django import forms
from django.contrib.auth.forms import UserCreationForm

from Profile.models import UserProfile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _




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



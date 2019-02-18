from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from Profile.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_pass(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError(
            _('The password must contain numbers'),
            params={'value': value},
        )
    elif len(value) < 8:
        raise ValidationError(
            _('The password must be at least 8 characters'),
            params={'value': value},
        )



# class SignUpForm(forms.ModelForm):
#     user_password = forms.CharField(widget=forms.PasswordInput, validators=[validate_pass])
#
#     class Meta:
#         model = User
#         fields = ('username' , 'first_name', 'last_name', 'user_password' , 'user_email' )
#
# class LogInForm(forms.ModelForm):
#     user_password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'user_password' )



class registerForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                 max_length=32, help_text='First name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                                max_length=32, help_text='Last name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64,
                             help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



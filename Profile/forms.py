from django import forms
from Profile.models import User
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



class SignUpForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput, validators=[validate_pass])

    class Meta:
        model = User
        fields = ('username' , 'first_name', 'last_name', 'user_password' , 'user_email' )

class LogInForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'user_password' )



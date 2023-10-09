from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        error_messages = {
            'first_name': {'required': 'Please enter a first name'},
            'last_name': {'required': 'Please enter a last name'},
            'email': {'required': 'Please enter an email address'},
            'password': {'required': 'Please enter a valid password'},
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'myclass', 'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'class': 'myclass', 'placeholder': 'Password'}),
        }
    



from django.contrib.auth.models import User
from .models import Profile
from django import forms

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class CustomRegForm(UserCreationForm):
    class Meta:
        model= User
        fields=UserCreationForm.Meta.fields

    username=forms.CharField(
        widget= forms.TextInput(
            attrs= {'class':'form-control',
            'placeholder':'Enter your Name'}
        )
    )

    password1=forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your password'
            }
        )
    )
    password2=forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirm your password'
            }
        )
    )

class CustomLoginForm(AuthenticationForm):
    username=forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control','placeholder':'Enter your UserName'}

        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(

            attrs={
                'class':'form-control', 'placeholder':'Enter your Password'
            }
        )
    )

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
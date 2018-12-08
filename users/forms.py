from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    firstname=forms.CharField(max_length=64)
    lastname=forms.CharField(max_length=64)
    email=forms.EmailField(max_length=254,help_text='Required for confirmation')
  

    class Meta:
        model=User
        fields =['firstname','lastname','username','email','password1','password2']

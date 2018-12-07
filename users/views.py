from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def userRegistrationForm(request):
    form=UserCreationForm()
    template = 'users/register.html'
    context ={
        'form':form
    }
    return render(request,template,context)

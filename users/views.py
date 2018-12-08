from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import SignupForm



# Create your views here.

def userRegistrationForm(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f' An account has been successfully created for You {username} ! You can now log in. ')
            return HttpResponseRedirect('/login/')
    else:
        form=SignupForm()
    template = 'users/register.html'
    context ={'form':form }
    return render(request,template,context)

def login(request):
    template='users/login.html'
    return render(request,template)
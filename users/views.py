from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import SignupForm



# Create your views here.
""" SignupForm was imported from forms and it replaced and it repalced UserCreationForm """

""" When the userRegistrationForm receives a request , if the request is a POST reqrest 
    a form is instanciated and it is populated by the post request."""
""" If the request is valid, the form is saved then the user is redirected to a login page """

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
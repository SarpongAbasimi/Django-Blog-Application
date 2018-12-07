from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def userRegistrationForm(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect('login-page')
    else:
        form=UserCreationForm()
    template = 'users/register.html'
    context ={'form':form }
    return render(request,template,context)

def login(request):
    template='users/login.html'
    return render(request,template)
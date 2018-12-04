from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.
def Home(request):
    template='home/home.html'
    return render(request,template)

def About(request):
    template='home/about.html'
    return render(request,template)

#Raise an expection when user being serch does not exit
def GetUser(request,userid):
    template='home/userid.html'
    try:
        getUser=User.objects.get(id=userid)
    except User.DoesNotExist:
        raise Http404("Sorry the user with that Id does not exist") 
    context={
        'getUser':getUser
    }
    return render(request,template,context)
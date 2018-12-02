from django.shortcuts import render

# Create your views here.
def Home(request):
    template='home/home.html'
    return render(request,template)

def About(request):
    template='home/about.html'
    return render(request,template)

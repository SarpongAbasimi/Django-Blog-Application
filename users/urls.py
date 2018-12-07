from django.urls import path
from .import views


urlpatterns= [
    path('register/',views.userRegistrationForm,name='user_registration'),
    path('login/',views.login,name='login-page')
]
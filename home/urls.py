from . import views
from django.urls import path

urlpatterns=[
    path('',views.Home,name='home-page'),
    path('about/',views.About,name='about-page'),
    path('<int:userid>/userid/',views.GetUser,name='user-id')
]

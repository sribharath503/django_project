from django.urls import path
from .views import *

urlpatterns=[
    path('',user_login,name='login'),
    path('user_logout/',user_logout,name='logout'),
    path('user_register/',user_register,name='register'),
]
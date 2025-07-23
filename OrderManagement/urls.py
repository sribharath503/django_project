from django.urls import path
from .views import *

urlpatterns=[
    path('add_customers/', add_customers),
    path('view_customers/', view_customers),
]
from django.urls import path
from .views import *

urlpatterns=[
    path('add_customers/', add_customers),
    path('view_customers/', view_customers),
    path('delete_customers/<int:id>/', delete_customers,name="delete_customers"),
    path('update_customers/<int:id>/', update_customers,name="update_customers"),
]
from django.urls import path
from .views import *

urlpatterns=[
    path('add_customers/', add_customers),
    path('view_customers/', view_customers),
    path('delete_customers/<int:id>/', delete_customers,name="delete_customers"),
    path('update_customers/<int:id>/', update_customers,name="update_customers"),
    path('add_orders/',add_orders),
    path('view_orders/',view_orders),
    path('delete_orders/<int:id>/',delete_orders,name='delete_order'),
    path('update_orders/<int:id>/',update_orders,name="update_order"),
]
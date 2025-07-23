from django.urls import path
from .views import *


urlpatterns = [
    path('home/', home),
    path('add_products/', add_products),
    path('view_products/', view_products),
    path('delete_product/<int:id>/',delete_product,name='delete_product'),
    path('update_product/<int:id>/',update_product,name='update_product'),
]
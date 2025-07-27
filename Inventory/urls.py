from django.urls import path
from .views import *


urlpatterns = [
    path('home/', home),
    #path('add_products/', add_products),
    #path('view_products/', view_products),
    #path('delete_product/<int:id>/',delete_product,name='delete_product'),
    #path('update_product/<int:id>/',update_product,name='update_product'),

    path('add_products/', add_product_view.as_view()),
    path('view_products/', view_product_view.as_view()),
    path('delete_product/<int:id>/',delete_product_view.as_view(),name='delete_product'),
    path('update_product/<int:id>/',update_product_view.as_view(),name='update_product'),
]
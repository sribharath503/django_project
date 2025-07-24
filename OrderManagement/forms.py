from django.forms import ModelForm
from .models import *

class customer_form(ModelForm):
    class Meta:
        model = customers
        fields = '__all__'

class order_form(ModelForm):
    class Meta:
        model= orders
        fields = ['customer','product','order_number','order_date','quantity']
from django import forms
from .models import *

class customer_form(forms.ModelForm):
    class Meta:
        model = customers
        fields = '__all__'

        widgets={
            'customer_name':forms.TextInput(attrs={'class':'form-control'}),
            'customer_since':forms.DateInput(attrs={'class':'form-control'}),
        }



class order_form(forms.ModelForm):
    class Meta:
        model= orders
        fields = ['customer','product','order_number','order_date','quantity']

        widgets={
           'customer':forms.Select(attrs={'class':'form-control'}),
           'product':forms.Select(attrs={'class':'form-control'}),
           'order_number':forms.NumberInput(attrs={'class':'form-control'}),
           'order_date':forms.DateInput(attrs={'class':'form-control'}),
           'quantity': forms.NumberInput(attrs={'class':'form-control'}),
           'amount':forms.NumberInput(attrs={'class':'form-control'}),
           'gst_amount':forms.NumberInput(attrs={'class':'form-control'}),
           'total_price':forms.NumberInput(attrs={'class':'form-control'}),
        }
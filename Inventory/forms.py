from django import forms
from .models import *

class product_form(forms.ModelForm):
    class Meta:
        model = products
        fields = '__all__'

        widgets={
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_code':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'gst':forms.NumberInput(attrs={'class':'form-control'}),
        }
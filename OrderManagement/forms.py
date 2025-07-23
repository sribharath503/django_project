from django.forms import ModelForm
from .models import customers

class customer_form(ModelForm):
    class Meta:
        model = customers
        fields = '__all__'
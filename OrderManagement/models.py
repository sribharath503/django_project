from django.db import models
from Inventory.models import products

# Create your models here.

class customers(models.Model):
    customer_name=models.CharField(max_length=100,null=True)
    customer_since=models.DateField(null=True)

    def __str__(self):
        return self.customer_name

class orders(models.Model):
    customer=models.ForeignKey(customers, on_delete=models.CASCADE)
    product=models.ForeignKey(products, on_delete=models.SET_NULL,null=True)
    order_number=models.IntegerField(null=True)
    order_date=models.DateField(null=True)
    quantity=models.IntegerField(null=True)
    amount=models.FloatField(null=True)
    gst_amount=models.FloatField(null=True)
    total_price=models.FloatField(null=True)

    def __str__(self):
        return self.order_number

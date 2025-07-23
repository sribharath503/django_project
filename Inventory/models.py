from django.db import models

# Create your models here.

class products(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    product_code=models.CharField(max_length=100,null=True)
    price=models.FloatField(default=0)
    gst=models.FloatField(default=0)

    def __str__(self):
        return self.product_name


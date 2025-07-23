from django.db import models

# Create your models here.

class customers(models.Model):
    customer_name=models.CharField(max_length=100,null=True)
    customer_since=models.DateField(null=True)

    def __str__(self):
        return self.customer_name

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    age=models.IntegerField(null=True)

    def __str__(self):
        return self.username
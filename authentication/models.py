from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    age=models.IntegerField(null=True)

    role_choice=(
        (0,'Admin'),
        (1,'Manager'),
        (2,'Employee')
    )

    role=models.IntegerField(default=0,choices=role_choice)

    def __str__(self):
        return self.username
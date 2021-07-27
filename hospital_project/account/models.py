from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser (AbstractUser):
    email = models.EmailField()
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    point = models.IntegerField(null=True)
    cert = models.FileField()
    h_name = models.CharField(max_length=30)
    ans_auth = models.BooleanField(default=False)
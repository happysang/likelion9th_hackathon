from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser (AbstractUser):
    #일반, 의사 공통
    email = models.EmailField()
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    #의사 한정
    h_name = models.CharField(max_length=30)
    cert = models.FileField()
    #둘다 생략
    point = models.IntegerField(null=True)
    ans_auth = models.BooleanField(default=False)
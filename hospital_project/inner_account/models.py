from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #일반, 의사 공통
    email = models.EmailField(unique = True)
    name = models.CharField(max_length=10)
    #의사 한정
    h_name = models.CharField(max_length=30)
    cert = models.FileField(upload_to="doctor_cert/%y/%m/%d", blank=True, null=True)
    #둘다 생략
    point = models.IntegerField(null=True)
    ans_auth = models.BooleanField(default=False)

    #unique = True 유일성여부


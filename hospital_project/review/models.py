from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageFieldFile
from django.conf import settings

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20)
    date = models.DateTimeField()
    hname = models.CharField(max_length=20)
    dname = models.CharField(max_length=10)
    dept = models.CharField(max_length=20)
    body = models.TextField(max_length=300)
    cert = models.ImageField(upload_to="review/%y/%m/%d", blank=True, null =True)
    likes_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
        
    def __str__(self):
        return self.title
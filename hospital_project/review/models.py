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
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name="like") #유익해요
    fun = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="fun") #재밌어요
    # ad = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True) #광고같아요
    upset = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="upset") #불쾌해요
    scrap = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="scrap") #불쾌해요

    def __str__(self):
        return self.title

from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageFieldFile
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20)
    date = models.DateTimeField()
    hname = models.CharField(max_length=20)
    dname = models.CharField(max_length=10)
    dept = models.CharField(max_length=20)
    body = models.TextField(max_length=300)
    doc = models.CharField(max_length=20, null=True) #의사가 글쓸 때 확인용
    cert = models.ImageField(upload_to="review/%y/%m/%d", blank=True, null =True)
    check = models.BooleanField(default=False) #의료 인증
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name="rlike") #유익해요
    fun = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="rfun") #재밌어요
    upset = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="rupset") #불쾌해요
    scrap = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="rscrap")
    # ad = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True) #광고같아요
    view_count =models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Rcomment(models.Model): 
    post=models.ForeignKey(Review, related_name='rcomments', on_delete=models.CASCADE) 
    author_name=models.CharField(max_length=20) 
    comment_text=models.TextField() 
    created_at=models.DateTimeField(default=timezone.now)
    doc = models.CharField(max_length=20, null=True)

    def approve(self): 
        self.save() 
    def __str__(self): 
        return self.comment_text
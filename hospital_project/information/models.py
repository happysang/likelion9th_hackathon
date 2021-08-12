from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Information(models.Model):
    title = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20)
    date = models.DateTimeField()
    dept = models.CharField(max_length=20)
    body = models.TextField(max_length=300)
    doc = models.CharField(max_length=20, null=True) #의사가 글쓸 때 확인용
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name="ilike") #유익해요
    fun = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="ifun") #재밌어요
    upset = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="iupset") #불쾌해요
    scrap = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="iscrap")
    view_count =models.IntegerField(default=0)

    # ad = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True) #광고같아요
    
    def __str__(self):
        return self.title

class Icomment(models.Model): 
    post=models.ForeignKey(Information, related_name='icomments', on_delete=models.CASCADE) 
    author_name=models.CharField(max_length=20) 
    comment_text=models.TextField() 
    created_at=models.DateTimeField(default=timezone.now)
    doc = models.CharField(max_length=20, null=True)
    def approve(self): 
        self.save() 
    def __str__(self): 
        return self.comment_text

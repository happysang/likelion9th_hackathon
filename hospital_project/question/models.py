from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20)
    date = models.DateTimeField()
    dept = models.CharField(max_length=20)
    body = models.TextField(max_length=300)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name="qlike") #유익해요
    fun = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="qfun") #재밌어요
    upset = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="qupset") #불쾌해요
    scrap = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="qscrap") #불쾌해요
    view_count =models.IntegerField(default=0)

    # ad = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True) #광고같아요
    
    def __str__(self):
        return self.title

class Qcomment(models.Model): 
    post=models.ForeignKey(Question, related_name='qcomments', on_delete=models.CASCADE) 
    author_name=models.CharField(max_length=20) 
    comment_text=models.TextField() 
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self): 
        self.save() 
    def __str__(self): 
        return self.comment_text

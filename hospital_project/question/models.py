from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    치과 = '치과',
    피부과 = '피부과',
    성형외과 = '성형외과',
    산부인과 = '산부인과',
    안과 = '안과',
    내과=  '내과',
    외과 = '외과',
    이비인후과 = '이비인후과',
    정형외과 ='정형외과',
    비뇨기과 = '비뇨기과',
    정신건강의학과 = '정신건강의학과',
    재활의학과 = '재활의학과',
    영상의학과 = '영상의학과',
    소아과 = '소아과',
    신경외과 = '신경외과',
    신경과 = '신경과',
    마취통층의학과 = '마취통층의학과',
    가정의학과 = '가정의학과',
    한의원 = '한의원'

    DEPT_CHOICES = (
        ('치과', '치과'),
        ('피부과', '피부과'),
        ('성형외과', '성형외과'),
        ('산부인과', '산부인과'),
        ('안과', '안과'),
        ('내과', '내과'),
        ('외과', '외과'),
        ('이비인후과', '이비인후과'),
        ('정형외과','정형외과'),
        ('비뇨기과', '비뇨기과'),
        ('정신건강의학과', '정신건강의학과'),
        ('재활의학과', '재활의학과'),
        ('영상의학과', '영상의학과'),
        ('소아과', '소아과'),
        ('신경외과', '신경외과'),
        ('신경과', '신경과'),
        ('마취통층의학과', '마취통층의학과'),
        ('가정의학과', '가정의학과'),
        ('한의원', '한의원')
    )
    dept = models.CharField(max_length=50, choices=DEPT_CHOICES)
    title = models.CharField(max_length=200)
    user_id = models.CharField(max_length=50)
    body = models.TextField(max_length=700)
    date = models.DateTimeField()
    view_count =models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model): 
    post=models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE) 
    author_name=models.CharField(max_length=20) 
    comment_text=models.TextField() 
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self): 
        self.save() 
    def __str__(self): 
        return self.comment_text


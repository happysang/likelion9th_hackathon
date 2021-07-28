from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Info(models.Model):
    dept = models.CharField(max_length = 100)
    user_id = models.CharField(max_length = 100)
    date = models.DateTimeField()
    title = models.CharField(max_length = 200)
    body = models.TextField()

    def __str__(self):
        return self.title

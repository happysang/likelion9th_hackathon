from django.contrib import admin
from .models import Question
from .models import Qcomment
# Register your models here.
admin.site.register(Question)
admin.site.register(Qcomment)

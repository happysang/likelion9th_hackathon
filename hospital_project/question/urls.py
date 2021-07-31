from django.urls import path
from question.views import *

urlpatterns = [
    path('qreadall', qreadall, name = "urlnameqreadall"),
    path('allq/', allq, name="urlnameallq"),
    path('<str:id>',detail,name="urlnamedetail"),
    path('new/',new,name="urlnamenew"),
    path('create/',create,name="urlnamecreate"),
    path('edit/<str:id>',edit,name="urlnameedit"),
    path('update/<str:id>',update,name="urlnameupdate"),
    path('question/comment/<str:id>', add_comment, name='urlnameadd_comment'),
    path('delete/<str:id>',delete,name="urlnamedelete"),

]

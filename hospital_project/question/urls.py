from django.urls import path
from question.views import *

urlpatterns = [
    path('',home,name="urlnamehome"),
    path('allq/', allq, name="urlnameallq"),
    path('<str:id>',detail,name="urlnamedetail"),
    path('edit/<str:id>',edit,name="urlnameedit"),
    path('update/<str:id>',update,name="urlnameupdate"),
    path('question/comment/<str:id>', add_comment, name='urlnameadd_comment'),

]

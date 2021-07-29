from django.urls import path
from information.views import *

urlpatterns = [
    path('', InfoList ,name = 'urlInfoList'),
    path('write/' , write , name ='urlwrite'),
    path('create/' , create , name='urlcreate'),
    path('detail/<int:Info_id>', detail, name='urldetail'),
]
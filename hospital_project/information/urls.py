from django.urls import path
from information.views import *

urlpatterns = [
    path('info', info, name = 'urlnameinfo'),
    path('readall', readall, name = 'urlnamereadall'),
    path('infodetail/<str:each_id>', infodetail, name = 'urlnameinfodetail'),
]

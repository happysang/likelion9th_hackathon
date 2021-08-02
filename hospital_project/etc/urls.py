from django.urls import path
from etc.views import *

urlpatterns = [
    path('',home, name = 'urlhome'),
    path('mypage/', mypage, name="urlmypage"),
    path('mypagedetail/', mypagedetail, name="urlmypagedetail"),
]

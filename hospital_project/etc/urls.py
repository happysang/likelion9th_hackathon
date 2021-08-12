from django.urls import path
from etc.views import *

urlpatterns = [
    path('',home, name = 'urlhome'),
    path('myscrap/<int:user_id>', myscrap ,name="myscrap"),
    path('mypage/', mypage, name="urlmypage"),
    path('mypagedetail/', mypagedetail, name="urlmypagedetail"),
    path('mypageobject/', myobject, name="urlmyobject"),
    path('search/', all_search_view, name="urlallsearch"),
    path('needlogin/', needlogin, name = "urlneedlogin")
]

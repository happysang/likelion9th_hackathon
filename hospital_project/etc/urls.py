from django.urls import path
from etc.views import *

urlpatterns = [
    path('',home, name = 'urlhome'),
    path('myprofile/<int:user_id>', myscrap ,name='myscrap'),
]

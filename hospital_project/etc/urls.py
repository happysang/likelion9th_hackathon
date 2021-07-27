from django.urls import path
from etc.views import *

urlpatterns = [
    path('',home, name = 'urlhome')
]

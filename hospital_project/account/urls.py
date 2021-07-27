from django.urls import path
from account.views import *

urlpatterns = [
    path('login/', login_view, name = 'urllogin'),
    path('signup/', signup_view, name = 'urlsignup'),
]
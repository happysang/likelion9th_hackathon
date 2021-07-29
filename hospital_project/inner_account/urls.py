from django.urls import path
from inner_account.views import *

urlpatterns = [
    path('login/', login_view, name = 'urllogin'),
    path('signup/<str:c>', signup_view, name = 'urlsignup'),
    path('choice/', choice, name = 'urlchoice'),
    path('popup/', popup, name="urlpopup"),
]
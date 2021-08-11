from django.urls import path
from inner_account.views import *

urlpatterns = [
    path('login/', login_view, name = 'urllogin'),
    path('signup/<str:c>', signup_view, name = 'urlsignup'),
    path('choice/', choice, name = 'urlchoice'),
    path('logout/', logout_view, name = 'urllogout'),
    path('activate/<str:uidb64>/<str:token>/', activate, name="activate"),
]
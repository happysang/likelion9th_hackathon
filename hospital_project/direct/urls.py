from django.urls import path
from direct.views import *

urlpatterns = [
   	path('inbox/', Inbox, name='inbox'),
   	path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send_direct'),
	path('new/', UserSearch, name='usersearch'),
	path('new/<username>', NewConversation, name='newconversation'),
	path('delete/<str:user>' , delete , name="delete" ),
]
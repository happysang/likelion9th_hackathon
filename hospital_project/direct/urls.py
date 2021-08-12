from django.urls import path
from direct.views import *

urlpatterns = [
   	path('inbox/', Inbox, name='urlinbox'),
   	path('directs/<username>', Directs, name='urldirects'),
    path('send/', SendDirect, name='urlsend_direct'),
	# path('new/', UserSearch, name='urlusersearch'),
	path('new/<username>', NewConversation, name='urlnewconversation'),
	path('delete/<str:user>' , delete , name="delete" ),
]

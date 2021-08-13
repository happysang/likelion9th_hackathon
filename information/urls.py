from django.urls import path
from information.views import *

urlpatterns = [
    path('category/', info_category_view, name = 'urlinfocategory'),
    path('detail<str:id>',info_detail_view,name='urlinfodetail'),
    path('readall/<int:d_num>',info_readall_view,name='urlinforeadall'),
    path('new/<int:d_num>', info_new_view, name='urlinfonew'),
    path('create/<int:d_num>', info_create_view, name='urlinfocreate'),
    path('edit/<str:id>', info_edit_view, name='urlinfoedit'),
    path('update/<str:id>', info_update_view, name='urlinfoupdate'),
    path('delete/<str:id>', info_delete_view, name='urlinfodelete'),
    path('like/', like, name='urlilike'),
    path('fun/', fun, name='urlifun'),
    path('upset/', upset, name='urliupset'),
    path('scrap/', scrap, name='urliscrap'),
    path('search/', info_search_view, name='urlinfosearch'),
   
]

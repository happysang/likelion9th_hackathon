from django.urls import path
from information.views import *

urlpatterns = [
    path('category', category, name = 'urlicategory'),
    path('', InfoList ,name = 'urlInfoList'),
    path('write/' , write , name ='urlwrite'),
    path('create/' , create , name='urlcreate'),
    path('detail/<str:Info_id>', detail, name='urldetail'),
    path('edit/<str:id>' , edit , name="urledit"),
    path('update/<str:id>' , update , name = "urlupdate"),
    path('delete/<str:id>' , delete , name = 'urldelete')
]
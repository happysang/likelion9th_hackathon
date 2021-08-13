from django.urls import path
from question.views import *

urlpatterns = [
    path('category/', question_category_view, name = 'urlquestioncategory'),
    path('detail<str:id>',question_detail_view,name='urlquestiondetail'),
    path('readall/<int:d_num>',question_readall_view,name='urlquestionreadall'),
    path('new/<int:d_num>', question_new_view, name='urlquestionnew'),
    path('create/<int:d_num>', question_create_view, name='urlquestioncreate'),
    path('edit/<str:id>', question_edit_view, name='urlquestionedit'),
    path('update/<str:id>', question_update_view, name='urlquestionupdate'),
    path('delete/<str:id>', question_delete_view, name='urlquestiondelete'),
    path('like/', like, name='urlqlike'),
    path('fun/', fun, name='urlqfun'),
    path('upset/', upset, name='urlqupset'),
    path('scrap/', scrap, name='urlqscrap'),
    path('search/', question_search_view, name='urlquestionsearch'),
]

from django.urls import path
from review.views import *

urlpatterns = [
    path('category/', review_category_view, name = 'urlreviewcategory'),
    path('detail<str:id>',review_detail_view,name='urlreviewdetail'),
    path('readall/<int:d_num>',review_readall_view,name='urlreviewreadall'),
    path('new/<int:d_num>', review_new_view, name='urlreviewnew'),
    path('create/<int:d_num>', review_create_view, name='urlreviewcreate'),
    path('edit/<str:id>', review_edit_view, name='urlreviewedit'),
    path('update/<str:id>', review_update_view, name='urlreviewupdate'),
    path('delete/<str:id>', review_delete_view, name='urlreviewdelete'),
    path('like/', like, name='urllike'),
    path('fun/', fun, name='urlfun'),
    path('upset/', upset, name='urlupset'),
    path('scrap/', scrap, name='urlscrap'),
    path('search/', review_search_view, name='urlreviewsearch'),

]
from django.urls import path
from review.views import *

urlpatterns = [
    path('review/detail<str:id>',review_detail_view,name='urlreviewdetail'),
    path('readall',review_readall_view,name='urlreviewreadall'),
    path('new/', review_new_view, name='urlreviewnew'),
    path('create/', review_create_view, name='urlreviewcreate'),
    path('edit/<str:id>', review_edit_view, name='urlreviewedit'),
    path('update/<str:id>', review_update_view, name='urlreviewupdate'),
    path('delete/<str:id>', review_delete_view, name='urlreviewdelete'),
    path('like/', video_like, name='video_like'),
]
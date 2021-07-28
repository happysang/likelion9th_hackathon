from django.urls import path
from review.views import *

urlpatterns = [
    path('review/detail<str:each_id>',review_detail_view,name='urlreviewdetail'),
    path('readall',review_readall_view,name='urlreviewreadall'),
]
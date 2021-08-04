from django.conf.urls import url
from django.urls.resolvers import URLPattern
from .import views

urlpattern = [
    url(r'^$' , views.index, name='index'),
]
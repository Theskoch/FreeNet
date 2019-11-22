from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    url(r'^post/addlikes/(?P<post_id>[0-9]+)/$', views.addlike, name='post')
]
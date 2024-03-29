from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^post/addlikes/(?P<post_id>[0-9]+)/$', views.addlike, name='post'),
    url(r'^accounts_user/$', views.user_info, name='ackaunt_user'),
    url(r'^accounts_logout/$', views.user_logout, name='logout'),

    path(r'post/<int:post_id>/', views.post_datail, name='post_datail'),
    
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'),name='login'),
]
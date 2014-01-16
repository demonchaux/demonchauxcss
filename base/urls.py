from django.conf.urls import patterns, include, url
from base import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
)
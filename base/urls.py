from django.conf.urls import patterns, url
from base import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^browse/(?P<type>\w+)/$', views.home_filter, name='home_filter'),
    url(r'^(?P<slug>[-\w]+)/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^event/(?P<event_id>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^biography/$', views.biography, name='biography')
)
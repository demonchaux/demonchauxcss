from django.conf.urls import patterns, include, url
from base.views import home

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
)
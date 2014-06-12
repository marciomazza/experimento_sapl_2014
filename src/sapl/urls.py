from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'home.views.login', name='login'),
    url(r'^logout/$', 'home.views.logout', name='logout'),
)

from crispy_forms.layout import Submit
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'home.views.login', name='login'),
    url(r'^logout/$', 'home.views.logout', name='logout'),
)

# ajuste (executado no inicio da aplicacao)
Submit.field_classes = 'btn btn-default'

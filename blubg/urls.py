# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'blubg.views.home', name='home'),
                       # url(r'^blubg/', include('blubg.foo.urls')),
                       url(r'^api/', include('blubg.api.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api import handlers


#Auth BASIC
auth = HttpBasicAuthentication(realm="Test Auth")
ad = { 'authentication': auth }

blog_handler = Resource(handler=handlers.BlogHandler,**ad)

urlpatterns = patterns('',
                       # Blog
                       url(r'^blog/(?P<blog_id>[^/]+)/$', blog_handler),
                       url(r'^blog/$', blog_handler),

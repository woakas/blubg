from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api_piston import handlers


#Auth BASIC
auth = HttpBasicAuthentication(realm="Test Auth")
ad = { 'authentication': auth }

blog_handler = Resource(handler=handlers.BlogHandler,**ad)
tag_handler = Resource(handler=handlers.TagHandler,**ad)

urlpatterns = patterns('',
                       # Blog
                       url(r'^blog/(?P<blog_id>[^/]+)/$', blog_handler),
                       url(r'^blog/$', blog_handler),
                       # Tag
                       url(r'^tag/(?P<tag_id>[^/]+)/$', tag_handler),
                       url(r'^tag/$', tag_handler),
                       # Post
                       url(r'^post/(?P<post_id>[^/]+)/$', tag_handler),
                       url(r'^post/$', tag_handler),
                       )

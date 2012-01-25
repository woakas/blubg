from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from api import BlogResource, TagResource, UserResource, TestResource


#Auth BASIC
#auth = HttpBasicAuthentication(realm="Test Auth")
#ad = { 'authentication': auth }
#ad = { }

v1_api = Api(api_name='v1')
v1_api.register(BlogResource())
v1_api.register(TagResource())
v1_api.register(UserResource())
v1_api.register(TestResource())

urlpatterns = patterns('',
                       # Blog
                       url(r'^', include(v1_api.urls)),
                       )

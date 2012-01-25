from django.conf.urls.defaults import patterns, url
from djangorestframework import views
from resources import BlogResource, UserResource



urlpatterns = patterns('',
                       url(r'^blog/$', views.ListOrCreateModelView.as_view(resource=BlogResource), name='blog-root'),
                       url(r'^blog/(?P<pk>[^/]+)/$', views.InstanceModelView.as_view(resource=BlogResource), name='blog-post'),

                       url(r'^user/$', views.ListOrCreateModelView.as_view(resource=UserResource), name='user-root'),
                       url(r'^user/(?P<pk>[^/]+)/$', views.InstanceModelView.as_view(resource=UserResource), name='user-post'),
                       

)

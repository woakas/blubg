from tastypie.resources import Resource, ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import Authorization
from blog import models

"""
POST
curl -H "Content-Type: application/json" -XPOST -d '{"name":"Prueba", "owner":"/api/tastypie/v1/user/1/"}' "http://127.0.0.1:8000/api/tastypie/v1/blog/"

GET
curl  "http://127.0.0.1:8000/api/tastypie/v1/blog/"
curl  "http://127.0.0.1:8000/api/tastypie/v1/blog/1/"
curl  "http://127.0.0.1:8000/api/tastypie/v1/blog/schema/"

"""


class TestResource(Resource):
    class Meta:
        qs = models.modelsAuth.User.objects.all()

    def dehydrate(self, bundle):
        bundle.data['custom_field'] = "Whatever you want"
        return bundle


class UserResource(ModelResource):
    
    class Meta:
        queryset = models.modelsAuth.User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        filtering = {
            'username': ALL,
            }

class BlogResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    class Meta:
        queryset = models.Blog.objects.all()
        resource_name = 'blog'
        filtering = {
            'owner': ALL_WITH_RELATIONS,
            'name': ['exact'],
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        authorization = Authorization()

    def dehydrate_name(self, bundle):
        return bundle.data['name'].upper()


class TagResource(ModelResource):

    class Meta:
        queryset = models.Tag.objects.all()
        resource_name = 'tag'

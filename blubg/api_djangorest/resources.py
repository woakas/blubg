from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from djangorestframework.views import View
from blog import models


class BlogResource(ModelResource):
    model = models.Blog
    fields = ('id','name', ('owner',('username','email',)))


#    def owner(self, instance):
#        return reverse('owner', kwargs={'blogpost': instance.key})

class UserResource(ModelResource):
    model = models.modelsAuth.User
    fields = ('username','email')



class OtherBlogView(View):
    
    def get(self, request):
        pass

from piston.handler import BaseHandler
from piston.utils import rc, throttle
from blog import models



class BlogHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE')
    model = models.Blog
    fields = ('name', 'id')
    
    def read(self, request, blog_id=None):
        base = models.Blog.objects
        
        if blog_id:
            try:
                return base.get(id=blog_id)
            except:
                return rc.NOT_FOUND
        else:
            return base.all() # Or base.filter(...)


    def update(self, request, blog_id):
        blog = models.Blog.objects.get(pk=blog_id)
        blog.name = request.PUT.get('name')
        blog.save()
        return blog


    def delete(self, request, blog_id):
        try:
            blog = models.Blog.objects.get(id=blog_id)
        except:
            return rc.NOT_FOUND
        if not request.user == blog.owner:
            return rc.FORBIDDEN 

        blog.delete()
        return rc.DELETED 


class TagHandler(BaseHandler):
    allowed_methods = ('GET', 'POST','PUT')
    model = models.Tag
    fields = ('name', 'description')
    
    def read(self, request, tag_id=None):
        base = models.Tag.objects
        
        if tag_id:
            try:
                return base.get(id=tag_id)
            except:
                return rc.NOT_FOUND
        else:
            return base.all() # Or base.filter(...)


    def update(self, request, tag_id):
        tag = models.Tag.objects.get(pk=tag_id)
        tag.name = request.PUT.get('name') or tag.name
        tag.description= request.PUT.get('description') or tag.description
        tag.save()
        return tag


    def create(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        if name and description:
            
            
            tag=models.Tag(name=name,description=description)
            tag.save()
            rc.CREATED
        else:
            rc.BAD_REQUEST

    

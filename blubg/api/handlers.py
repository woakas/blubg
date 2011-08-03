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

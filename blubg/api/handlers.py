from piston.handler import BaseHandler
from piston.utils import rc, throttle
from blog import models



class BlogHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE')
    model = models.Blog
    fields = ('name', )
    
    def read(self, request, blog_id=None):
        base = models.Blog.objects
        
        if blog_id:
            return base.get(pk=blog_id)
        else:
            return base.all() # Or base.filter(...)


    def update(self, request, blog_id):
        blog = Blog.objects.get(pk=blog_id)
        blog.title = request.PUT.get('name')
        blog.save()
        return blog


    def delete(self, request, blog_id):
        blog = Blog.objects.get(pk=blog_id)
        if not request.user == blog.owner:
            return rc.FORBIDDEN 

        blog.delete()
        return rc.DELETED 

from piston.handler import BaseHandler
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

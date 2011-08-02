from django.db import models
from django.contrib.auth import models as modelsAuth
import datetime

class Blog(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(modelsAuth.User)
    
    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Title', max_length=30)
    description = models.TextField('Description')
    
    def __unicode__(self):
        return self.name
    

class Post(models.Model):
    tags = models.ManyToManyField(Tag,blank=True)
    blog = models.ForeignKey(Blog)
    title = models.CharField('Title', max_length=30)
    date = models.DateTimeField('Date',default=datetime.datetime.now()) 
    content = models.TextField('Content')
    
    def __unicode__(self):
        return self.title

    
class Comment(models.Model):
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post)
    date = models.DateTimeField('Date',default=datetime.datetime.now())
    
    def __unicode__(self):
        return self.date

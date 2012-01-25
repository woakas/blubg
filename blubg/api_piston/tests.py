# -*- coding: utf-8 -*-
from django.contrib.auth import models as modelsAuth
from django.test import TestCase
from django.test.client import Client
from blog import models
import base64


class ApiAuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = modelsAuth.User.objects.create_user('admin',
                                                        'admin@test.com',
                                                        'admin')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.save()
        user = 'admin:admin'
        self.auth_string = 'Basic %s' % base64.encodestring(user).rstrip()
        auth = 'Basic %s' % base64.encodestring("admin:admin").strip()
        self.extra = {
            'HTTP_AUTHORIZATION': auth,
        }

    def tearDown(self):
        self.user.delete()


class TestAPIAuth(ApiAuthTest):

    def testFailUser(self):
        user = 'adminn:admin'
        bad_auth_string = 'Basic %s' % base64.encodestring(user).strip()
        response = self.client.get('/api/piston/blog/', {},
                                   HTTP_AUTHORIZATION=bad_auth_string)
        self.assertEquals(response.status_code, 401)

    def testOkUser(self):
        response = self.client.get('/api/piston/blog/', {}, **self.extra)
        self.assertEqual(response.status_code, 200)

    def testMultiplesUsers(self):
        users = (('admin', 'admin!'),
                 ('admin', 'secr3t'),
                 ('admin', 'user'),
                 ('admin', 'allwork'),
                 ('admin', 'thisisneat'))
        for username, password in users:
            auth_string = 'Basic %s' % base64.encodestring(
                '%s:%s' % (username, password)).rstrip()
            response = self.client.get('/api/piston/blog/',
                                       HTTP_AUTHORIZATION=auth_string)
            self.assertEquals(response.status_code, 401,
                              'Failed with login of %s:%s'
                              % (username, password))


class BlogTest(ApiAuthTest):
    def setUp(self):
        super(BlogTest, self).setUp()
        self.blog1 = models.Blog.objects.create(name = u"Gestión y Desarrollo",
                                                owner = self.user)

    def tearDown(self):
        super(BlogTest, self).tearDown()
        self.blog1.delete()

    def testCreateBlog(self):
        response = self.client.post("/api/piston/blog/",
                                    {"name" : "Blog Test1",
                                     "owner" : self.user.id},
                                    **self.extra)
        self.assertEqual(response.status_code, 405)

    def testGetBlog(self):
        result="""{
    "name": "Gestión y Desarrollo", 
    "id": 1
}"""
        response = self.client.get('/api/piston/blog/%d/'%(self.blog1.id), {}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.content, result)

    def testUpdateBlog(self):
        response = self.client.put('/api/piston/blog/%d/' % (self.blog1.id), {'name':'Test Blog Rename'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(models.Blog.objects.get(id=1).name,"Test Blog Rename")
        
    def testDeleteBlog(self):
        response = self.client.delete('/api/piston/blog/%d/'%(self.blog1.id), {}, **self.extra)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(models.Blog.objects.all()),0)

class TagTest(ApiAuthTest):    
    def setUp(self):
        super(TagTest, self).setUp()
        self.tag=models.Tag.objects.create(name = u"Desarrollo",
                                           description = "Tag de Desarrollo")

    def tearDown(self):
        super(TagTest, self).tearDown()
        self.tag.delete()
    
    def testCreateTag(self):
        response = self.client.post('/api/piston/tag/', {'name':"Django",'description':'Tag for Django'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Tag.objects.get(name='Django').description,"Tag for Django")

    def testGetTag(self):
        result="""{
    "name": "Desarrollo", 
    "description": "Tag de Desarrollo"
}"""
        response = self.client.get('/api/piston/tag/%d/'%(self.tag.id), {}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.content, result)

    def testUpdateTag(self):
        response = self.client.put('/api/piston/tag/%d/'%(self.tag.id), {'name':'Test Tag Rename'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Tag.objects.get(id=1).name,"Test Tag Rename")
        self.assertEqual(models.Tag.objects.get(id=1).description,"Tag de Desarrollo")
        
        response = self.client.put('/api/piston/tag/%d/'%(self.tag.id), {'description':'New Description'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Tag.objects.get(id=1).name,"Test Tag Rename")
        self.assertEqual(models.Tag.objects.get(id=1).description,"New Description")

    def testDeleteTag(self):
        response = self.client.delete('/api/piston/tag/%d/'%(self.tag.id), {}, **self.extra)
        self.assertEqual(response.status_code, 405)


class PostTest(ApiAuthTest):    
    def setUp(self):
        super(PostTest, self).setUp()
        self.post=models.Post.objects.create(name = u"Desarrollo",
                                             description = "Post de Desarrollo")

    def tearDown(self):
        super(PostTest, self).tearDown()
        self.post.delete()
    
    def testCreatePost(self):
        response = self.client.post('/api/piston/post/', {'name':"Django",'description':'Post for Django'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Post.objects.get(name='Django').description,"Post for Django")

    def testGetPost(self):
        result="""{
    "name": "Desarrollo", 
    "description": "Post de Desarrollo"
}"""
        response = self.client.get('/api/piston/post/%d/'%(self.post.id), {}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.content, result)

    def testUpdatePost(self):
        response = self.client.put('/api/piston/post/%d/'%(self.post.id), {'name':'Test Post Rename'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Post.objects.get(id=1).name,"Test Post Rename")
        self.assertEqual(models.Post.objects.get(id=1).description,"Post de Desarrollo")
        
        response = self.client.put('/api/piston/post/%d/'%(self.post.id), {'description':'New Description'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Post.objects.get(id=1).name,"Test Post Rename")
        self.assertEqual(models.Post.objects.get(id=1).description,"New Description")

    def testDeletePost(self):
        response = self.client.delete('/api/piston/post/%d/'%(self.post.id), {}, **self.extra)
        self.assertEqual(response.status_code, 405)
        

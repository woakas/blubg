# -*- coding: utf-8 -*-
from django.contrib.auth import models as modelsAuth
from django.test import TestCase
from blog import models
import base64

class AppliTest(TestCase):
    def setUp(self):
        self.user = modelsAuth.User.objects.create_user('admin', 'admin@test.com', 'admin')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.save()
        self.auth_string = 'Basic %s' % base64.encodestring('admin:admin').rstrip()
        
    def tearDown(self):
        self.user.delete()


class BlogTest(AppliTest):
    def setUp(self):
        super(BlogTest, self).setUp()
        self.blog1=models.Blog.objects.create(name = u"Gestión y Desarrollo",
                                              owner = self.user)
        self.blog2=models.Blog.objects.create(name = u"Creación y Tareas",
                                              owner = self.user) 
        
        
    def tearDown(self):
        super(BlogTest, self).tearDown()
        self.blog1.delete()
        self.blog2.delete()


        
    def test_unicode(self):
        self.assertEqual(unicode(self.blog1), u"Gestión y Desarrollo")
        self.assertEqual(unicode(self.blog2), u"Creación y Tareas")
        
    
    
        
    

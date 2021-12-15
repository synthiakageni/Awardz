from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Project,User

# Create your tests here.
class ProjectTestClass(TestCase):
    #setuo method
    def setUp(self):
        self.user = User(username='synthia')
        self.synthia = Project(title = 'sweet', url='http://sweet.com', description = 'sweets are sweet', user = self.user, photo = 'default.png', date = '12-12-2021')
        
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.synthia,Project))
        
    def test_save_method(self):
        self.synthia.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)    
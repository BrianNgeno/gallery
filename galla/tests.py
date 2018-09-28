from django.test import TestCase
from .models import Editor,Categorys,Image,Location 
# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.brian= Editor(first_name = 'Brian', last_name ='Ngeno', email ='bkn.ngeno@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.brian,Editor))
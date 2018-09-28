from django.test import TestCase
from .models import Editor,Categorys,Image,Location 
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.brian= Editor(first_name = 'Brian', last_name ='Ngeno', email ='bkn.ngeno@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.brian,Editor))
    # Testing Save Method
    '''
    test save editor
    '''
    def test_save_method(self):
        self.brian.save_editor()
        editor = Editor.objects.all()
        self.assertTrue(len(editor)>0)

    '''
    test delete editor
    '''

    def test_delete_method(self):
        self.brian.save_editor()
        self.brian.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)==0)

class ImageTestCLass(TestCase):
    '''
    setup self instance of Article
    '''
    def setUp(self):
        Brian = Editor(first_name='Brian',last_name='Ngeno',email='bkn.ngeno@gmail.com')
        Brian.save_editor()
        self.pic = Image(name='Music',description='music is a southing sound that moves souls',editor=Brian)
    
    ''' 
    test instance of article
    '''
    def test_instance(self):
       self.assertTrue(isinstance(self.pic,Image))


#     # def tearDown(self):
    #    Article.objects.all().delete()
    '''
    test save article
    '''

    def test_save_image(self):
        self.pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    '''
    test delete article
    '''

    def test_delete_image(self):
        self.pic.save_image()
        self.pic.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
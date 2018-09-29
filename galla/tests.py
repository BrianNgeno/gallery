from django.test import TestCase
from .models import Categorys,Image,Location 
import datetime as dt
# Create your tests here.

class ImageTestCLass(TestCase):
    '''
    setup self instance of Article
    '''
    def setUp(self):
        self.pic = Image(name='Music',description='music is a southing sound that moves souls')
    
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

    def test_get_news_today(self):
        today_images = Image.todays_images()
        self.assertTrue(len(today_images)>0)
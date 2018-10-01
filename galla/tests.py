from django.test import TestCase
from .models import Categorys,Image,Location 
import datetime as dt
# Create your tests here.

class ImageTestCLass(TestCase):
    '''
    setup self instance of image
    '''
    def setUp(self):
        self.pic = Image(name='Music',description='music is a southing sound that moves souls')
    
    ''' 
    test instance of image
    '''
    def test_instance(self):
       self.assertTrue(isinstance(self.pic,Image))


    '''
    test save image
    '''

    def test_save_image(self):
        self.pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    '''
    test delete image
    '''

    def test_delete_image(self):
        self.pic.save_image()
        self.pic.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_get_image_today(self):
        today_images = Image.todays_images()
        self.assertTrue(len(today_images)>0)

class CategorysTestClass(TestCase):
    '''
    test setup of Categorys
    '''
    def setUp(self):
        self.New = Categorys(name='New')

    '''
    test instance of category
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.New,Categorys))

    # def tearDown(self):
    #     Tags.objects.all().delete()
    '''
    test to assertain save category
    '''
    def test_save_category(self):
        self.New.save_category()
        cat = Categorys.objects.all()
        self.assertTrue(len(cat)>0)
    '''
    test to assert that delete is working
    '''
    def test_delete_category(self):
        self.New.save_category()
        self.New.delete_category()
        cat = Categorys.objects.all()
        self.assertTrue(len(cat)== 0)

    '''
    test to assert that categorys update
    '''
    def test_update_category(self):
        self.New.save_category()
        new = Categorys.objects.filter(name='New').update(name='outdated')
        cat = Categorys.objects.get(name='outdated')
        self.assertEqual(cat.name,'outdated')   

class LocationTestClass(TestCase):
    '''
    test setup of Location
    '''
    def setUp(self):
        self.New = Location(name='New')

    '''
    test instance of Location
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.New,Location))

    # def tearDown(self):
    #     Tags.objects.all().delete()
    '''
    test to assertain save Location
    '''
    def test_save_location(self):
        self.New.save_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)>0)
    '''
    test to assert that delete is working
    '''
    def test_delete_location(self):
        self.New.save_location()
        self.New.delete_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)== 0)

    '''
    test to assert that Location update
    '''
    def test_update_location(self):
        self.New.save_location()
        new = Location.objects.filter(name='New').update(name='outdated')
        loc = Location.objects.get(name='outdated')
        self.assertEqual(loc.name,'outdated')  
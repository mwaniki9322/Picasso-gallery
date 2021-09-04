from gallery.models import Category, Image, Locations
from django.test import TestCase

# Create your tests here.

class LocationTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.nairobi= Locations(name='Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Locations))

    # Testing Save Method
    def test_save_method(self):
        self.nairobi.save_location()
        locations = Locations.objects.all()
        self.assertTrue(len(locations) > 0)

#category tests
class CategoryTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.hiking= Category(name='Hiking')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hiking,Category))

    # Testing Save Method
    def test_save_method(self):
        self.hiking.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

#image test

class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.image= Image(image_name='Hiking',image_description='rrr')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

    




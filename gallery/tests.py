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
    
    def setUp(self):
        # Creating a new location and saving it
        self.new_location = Locations(name = 'Nairobi')
        self.new_location.save()

        # Creating a new category and saving it
        self.new_category = Category(name = 'Category')
        self.new_category.save()

        self.new_image= Image(image_name = 'BMW',image_description = 'Nice sports car',location = self.new_location,Category=self.new_category)

        self.new_image.save()


    def tearDown(self):
        Image.objects.all().delete()
        Locations.objects.all().delete()
        Category.objects.all().delete()

    def test_get_images(self):
        images = Image.get_images()
        self.assertTrue(len(images)>0)




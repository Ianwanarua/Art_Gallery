from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(cat_name='Nature')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0) 

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)
        
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locat = Location.objects.all()
        self.assertTrue(len(locat) > 0) 

    def test_delete_location(self):
        self.location.delete_location()
        category = Location.objects.all()
        self.assertTrue(len(category) == 0)
    
    def test_get_location(self):
        location = Location.get_locations()
        self.assertTrue(location)
        
class ImageTestClass(TestCase):

    def setUp(self):

        self.location = Location(location_name='Nairobi')
        self.location.save_location()

        self.category = Category(cat_name='Mountains')
        self.category.save_category()

        self.mountain= Image(id=1,image_name = 'Mountains', description ='Mountain Test',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.mountain,Image))
    
    def test_save_image(self):
        self.mountain.save_image()
        img = Image.objects.all()
        self.assertTrue(len(img) > 0)

    def test_delete_image(self):
        self.mountain.delete_image()
        img = Image.objects.all()
        self.assertTrue(len(img)== 0)
    
    def test_update_img(self):
        self.mountain.save_image()
        self.mountain.update_img(self.mountain.id, 'images/img.jpg')
        new_img = Image.objects.filter(image='images/img1.jpg')
        self.assertFalse(len(new_img) > 0)

    def test_get_image_by_id(self):
        self.mountain.save_image()
        img = self.mountain.get_image_by_id(self.mountain.id)
        images = Image.objects.filter(id=self.mountain.id)
        self.assertTrue(img, images)    

    def test_search_by_category(self):
        category = 'Nature'
        found_img = self.mountain.search_by_category(category)
        self.assertFalse(len(found_img) > 1)  
    
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
from django.test import TestCase
from .models import Profile,Image
import datetime as dt


# Create your tests here.
class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile(profile_photo="'image.jpeg'",bio="God Above All")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    #Testing Save Method
    def test_save_method(self):
        self.new_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()

# class ImageTestClass(TestCase):
#
#     def setUp(self):
#         # Creating a new category and saving it
#         self.new_category= Category(name = 'Design')
#         self.new_category.save_category()
#
#         # Creating a new location and saving it
#         self.new_location= Location(name = 'Nairobi')
#         self.new_location.save_location()
#
#         self.new_image= Image(image='image.jpeg',name = 'Test Image',description = 'This is a random test Image description',category = self.new_category,location=self.new_location)
#         self.new_image.save()

        # self.new_image.category.add(self.new_category)
        # self.new_image.category.add(self.new_location)


    # def tearDown(self):
    #     Category.objects.all().delete()
    #     Location.objects.all().delete()
    #     Image.objects.all().delete()
    #
    # def test_instance(self):
    #     self.assertTrue(isinstance(self.new_image,Image))
    #
    # def test_save_method(self):
    #     images = Image.objects.all()
    #     self.assertTrue(len(images)>0)
    #
    # def test_delete_method(self):
    #     self.new_image.save_image()
    #     self.new_image.delete_image()


        # self.design.save_category()
        # self.design.delete_category()

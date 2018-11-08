from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "profile")
    profile_photo=models.ImageField(upload_to='profiles',blank=True)
    bio=models.TextField()

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image=models.ImageField(upload_to ='images/', blank = True)
    name=models.CharField(max_length =30)
    caption=models.TextField(blank=True,null=True)
    profile=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(blank=True,null=True)
    comments=models.TextField(blank=True,null=True)

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()


    @classmethod
    def get_photos(cls):
        photos=cls.objects.all()
        return photos

    @classmethod
    def get_image_by_id(cls,image_id):
        image=cls.objects.get(id=image_id)
        return image

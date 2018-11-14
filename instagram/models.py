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

    @classmethod
    def get_profile_by_id(cls,image_id):
        profile=cls.objects.get(id=profile_id)
        return profile

    @classmethod
    def search_by_user(cls,search_term):
        instagram=cls.objects.filter(user__username=search_term)
        return instagram



class Like(models.Model):

    image=models.ImageField(upload_to ='images/', blank = True)
    name=models.CharField(max_length =30)
    caption=models.TextField(blank=True,null=True)

    @classmethod
    def get_likes(cls):
        photos=cls.objects.all()
        return photos

class Image(models.Model):
    image=models.ImageField(upload_to ='images/', blank = True)
    name=models.CharField(max_length =30)
    caption=models.TextField(blank=True,null=True)
    profile=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(blank=True,null=True)
    # comments=models.ForeignKey(Comment)

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


class Comment(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
    commenter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length =30)

    @classmethod
    def get_comments(cls,image_id):
        comments=cls.objects.filter(id=image_id)
        return comments

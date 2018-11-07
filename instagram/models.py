from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profiles')
    profile_name=models.CharField(max_length =30)
    bio=models.TextField()

    # def save_profile(self):
    #     self.save()
    # def delete_profile(self):
    #     self.delete()

class Image(models.Model):
    image=models.ImageField(upload_to ='images/')
    image_name=models.CharField(max_length =30)
    image_caption=models.TextField()
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)
    # likes=models.
    # Comments

    # def save_image(self):
    #     self.save()
    # def delete_image(self):
    #     self.delete()

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=300)
    cafedra = models.CharField(max_length=300)
    level = models.CharField(max_length=200)
    avatar = models.ImageField(default="profile_img.jpeg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path) 

        if img.width>300 or img.height>300:
            output=(300, 300)
            img.thumbnail(output)
            img.save(self.avatar.path)
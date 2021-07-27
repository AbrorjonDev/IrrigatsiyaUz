from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField

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


class Contact(models.Model):
    email = models.EmailField()
    phone = PhoneNumberField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'
    
    def __str__(self):
        return f'{self.subject}'
    

class AdminContactPhones(models.Model):
    phone = PhoneNumberField()
    class Meta:
        managed = True
        verbose_name = 'Contact Phone'
        verbose_name_plural = 'Contact Phones'
    
    def __str__(self):
        return self.phone

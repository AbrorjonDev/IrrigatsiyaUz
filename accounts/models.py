from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.CharField(_('faculty'), max_length=300)
    cafedra = models.CharField(_('cafedra'), max_length=300)
    level = models.CharField(_('level'), max_length=200)
    avatar = models.ImageField(_('avatar'), default="profile_img.jpeg", upload_to="profile_pics")

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
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages') 
    
    def __str__(self):
        return f'{self.subject}'
    

class AdminContactPhones(models.Model):
    phone = PhoneNumberField()
    class Meta:
        managed = True
        verbose_name = _('Contact Phone')
        verbose_name_plural = _('Contact Phones')
    
    def __str__(self):
        return f'{self.phone}'

class AddressLink(models.Model):
    name = models.CharField(_('name'), max_length=500)
    link = models.URLField(blank=False, null=False)

    class Meta:
        verbose_name = _('Address Link')
        verbose_name_plural = _('Address Links')

    def __str__(self):
        return self.name
    


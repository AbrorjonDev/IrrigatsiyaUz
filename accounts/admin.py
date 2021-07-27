from django.contrib import admin
from .models import  Profile, Contact, AdminContactPhones

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact)
admin.site.register(AdminContactPhones)


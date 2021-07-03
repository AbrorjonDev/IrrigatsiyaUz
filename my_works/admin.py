from django.contrib import admin
from .models import MyWorks

class MyWorksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'id', 'file', 'author', 'date_published', 'date_updated')
    list_filter = ('category','date_published', 'date_updated')

admin.site.register(MyWorks, MyWorksAdmin)

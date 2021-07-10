from django.contrib import admin
from .models import (
    Articles,
    Books, 
    Presentations,
    Projects, 
    Events,
    Videos,
    )

class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'id', 'file', 'author', 'date_published', 'date_updated')
    list_filter = ('date_published', 'date_updated')

admin.site.register(Articles, ArticlesAdmin)

class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'id', 'file', 'author', 'date_published', 'date_updated')
    list_filter = ('date_published', 'date_updated')

admin.site.register(Books, BooksAdmin)

class PresentationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'id', 'file', 'author', 'date_published', 'date_updated')
    list_filter = ('date_published', 'date_updated')

admin.site.register(Presentations, PresentationsAdmin)

class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'id', 'file', 'author', 'date_published', 'date_updated')
    list_filter = ('date_published', 'date_updated')

admin.site.register(Projects, ProjectsAdmin)

class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'id', 'file', 'author', 'date_published', 'date_updated')
    list_filter = ('date_published', 'date_updated')

admin.site.register(Events, EventsAdmin)

class VideosAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'id', 'file', 'author', 'date_published', 'date_updated')
    list_filter = ('date_published', 'date_updated')

admin.site.register(Videos, VideosAdmin)
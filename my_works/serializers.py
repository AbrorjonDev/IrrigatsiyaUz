from rest_framework import serializers
from .models import (
    Articles,
    Books, 
    Presentations,
    Projects, 
    Events,
    Videos,
    )
import re
class ArticlesSerializers(serializers.ModelSerializer):
     
    class Meta:
        model = Articles
        fields = ('slug', 'name','name_uz', 'name_en','name_ru',  
                'file', 'link', 'author', 
                'date_published', 'date_updated')
        extra_kwargs = {
            'date_published':{'read_only':True},
            'slug':{'read_only':True},
            'author':{'read_only':True},

            }

    def create(self, validated_data):
        return Articles.objects.create(**validated_data, author_id=1)         

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


class BooksSerializers(serializers.ModelSerializer):
     
    class Meta:
        model = Books
        fields = ('slug', 'name','name_uz', 'name_en','name_ru', 
                'file', 'link', 'author', 
                'date_published', 'date_updated')
        extra_kwargs = {
            'date_published':{'read_only':True},
            'slug':{'read_only':True},

            }
    def create(self, validated_data):
        return Books.objects.create(**validated_data, author_id=1)         

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


class PresentationsSerializers(serializers.ModelSerializer):
     
    class Meta:
        model = Presentations
        fields = ('slug', 'name','name_uz', 'name_en','name_ru',  
            'file', 'link', 'author', 
            'date_published', 'date_updated')
        extra_kwargs = {
            'date_published':{'read_only':True},
            'slug':{'read_only':True},
            'author':{'read_only':True},
            }
    def create(self, validated_data):
        return Presentations.objects.create(**validated_data, author_id=1)         

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


class ProjectsSerializers(serializers.ModelSerializer):
     
    class Meta:
        model = Projects
        fields = ('slug', 'name','name_uz', 'name_en','name_ru', 
                'file', 'link', 'author', 
                'date_published', 'date_updated')
        extra_kwargs = {
            'date_published':{'read_only':True},
            'slug':{'read_only':True},
            'author':{'read_only':True},

            }
    def create(self, validated_data):
        return Projects.objects.create(**validated_data, author_id=1)         

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


class EventsSerializers(serializers.ModelSerializer):
     
    class Meta:
        model = Events
        fields = ('slug', 'name','name_uz', 'name_en','name_ru', 
                'file', 'link', 'author', 
                'date_published', 'date_updated')
        extra_kwargs = {
            'date_published':{'read_only':True},
            'slug':{'read_only':True},
            'author':{'read_only':True}

            }
    def create(self, validated_data):
        return Events.objects.create(**validated_data, author_id=1)         

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


class VideosSerializers(serializers.ModelSerializer):
     
    class Meta:
        model = Videos
        fields = ('slug', 'name','name_uz', 'name_en','name_ru', 
            'file', 'link', 'author', 
            'date_published', 'date_updated')
        extra_kwargs = {
            'date_published':{'read_only':True},
            'slug':{'read_only':True},
            'author':{'read_only':True}
            }

    def link_management(self, validated_data):
        link = validated_data.get('link')
        
        if link:
            if not link.find('https://youtube.com/embed/'):
                return link  
            elif link.find('youtu.be'):
                res = link.find('youtu.be/')
                result = link[:res] + 'youtube.com/embed/' + link[(res+9):]
                link = result
                return link
    def create(self, validated_data):
        name = validated_data.get('name')
        file = validated_data.get('file')
        return Videos.objects.create(name=name, file=file, link=self.link_management(validated_data=validated_data), author_id=1)         
    

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.link = self.link_management(validated_data=validated_data)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


from rest_framework import serializers
from .models import MyWorks


class MyWorksSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = MyWorks
        fields = ('category', 'name', 
                'file', 'link', 'author', 
                'date_published', 'date_updated')

    def create(self, validated_data):
        return MyWorks.objects.create(**validated_data, author_id=2)         

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


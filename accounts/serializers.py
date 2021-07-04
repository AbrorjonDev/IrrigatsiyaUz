from rest_framework import serializers
from .models import Profile
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import User
from drf_writable_nested.serializers import WritableNestedModelSerializer #for updating profile 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        extra_kwargs = {
			'username':{
				'validators':[UnicodeUsernameValidator()]
			}
		}
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user', 'faculty', 'cafedra', 'level', 'avatar')
        related_object = 'user'

    def update(self, instance, validated_data):

        user_data = validated_data.pop('user')
        instance.user = validated_data.get('user', user_data)
        instance.faculty = validated_data.get('faculty', instance.faculty)
        instance.cafedra = validated_data.get('cafedra', instance.cafedra)
        instance.level = validated_data.get('level', instance.level)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance
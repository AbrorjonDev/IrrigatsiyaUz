from rest_framework import serializers
from .models import Profile
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import User

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
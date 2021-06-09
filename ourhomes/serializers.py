from rest_framework import serializers
from .models import *
from .models import User

# define serializers
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields="__all__"

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields="__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name' ,'username', 'email', 'password', 'is_admin', 'is_homemanager', 'is_user']


    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_admin=validated_data['is_admin'],
            is_homemanager=validated_data['is_homemanager'],
            is_user=validated_data['is_user'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
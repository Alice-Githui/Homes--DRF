from rest_framework import serializers
from .models import *

# define serializers
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields="__all__"

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields="__all__"


class ProfileRegistrationSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField(
        min_length=8,
        max_length=20,
        write_only=True,
        error_messages={
            "min_length": "Password should be atleast {min_length} characters"
        }

    )
    confirmpassword=serializers.CharField(
        min_length=8,
        max_length=20,
        write_only=True,
        error_messages={
            "min_length": "Password should be atleast {min_length} characters"
        }
    )
    location=serializers.CharField()

    class Meta:
        model=Profile
        fields="__all__"

    def create(self, validated_data):
        profile=Profile.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            location=validated_data['location']
        )
        profile.set_password(validated_data['password'])
        profile.save()
        return profile
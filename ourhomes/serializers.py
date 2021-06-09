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
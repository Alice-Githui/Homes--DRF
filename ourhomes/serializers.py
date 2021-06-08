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
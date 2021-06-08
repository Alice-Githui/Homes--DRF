from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class LocationList(APIView):
    serializer_class=LocationSerializer

    #get all the locations
    def get(self, request, format=None):
        locations=Location.objects.all()
        serializers=LocationSerializer(locations, many=True)
        return Response(serializers.data)

    # post a new location
    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            locations=serializers.data

            response={
                "data":{
                    "newlocation": dict(locations),
                    "status":"Success",
                    "message":"New Location created successfully"
                }
            }
            
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

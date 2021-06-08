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

class LocationDetails(APIView):
    # get one neighbourhood 
    def get_location(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format=None):
        location=self.get_location(pk)
        serializers=LocationSerializer(location)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        location=self.get_location(pk)
        serializers=LocationSerializer(location, request.data)
        if serializers.is_valid():
            serializers.save()
            location=serializers.data

            response={
                "data":{
                    "updatedlocation":dict(location),
                    "success":"Success",
                    "message":"Location updated successfully"
                }
            }
            return Response(location)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        location=self.get_location(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HomeList(APIView):
    serializer_class=HomeSerializer

    def get(self, request, format=None):
        home=Home.objects.all()
        serializers=HomeSerializer(home, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            home=serializers.data

            response={
                "data":{
                    "newhome":dict(home),
                    "status":"Success",
                    "message":"New Home created successfully"
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(status.error, status=status.HTTP_400_BAD_REQUEST)

class HomeDetails(APIView):
    # get one home using id

    def get_home(self, pk):
        try:
            return Home.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format=None):
        home=self.get_home(pk)
        serializers=HomeSerializer(home)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        home=self.get_home(pk)
        serializers=HomeSerializer(home, request.data)
        if serializers.is_valid():
            serializers.save()
            home=serializers.data

            return Response(home)
        return Response(status.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        home=self.get_home(pk)
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
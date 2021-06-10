from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import FileUploadParser

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

    def post(self, request, *args, **kwargs):
        images=request.data['profile']
        name=request.data['name']
        capacity=request.data['capacity']
        # location=request.data['location']
        Home.objects.create(images=images, name=name, capacity=capacity)
        return HttpResponse({'message':'New Home created'}, status=status.HTTP_200_OK)

    # parser_class=(FileUploadParser,)
    # def post(self, request, format=None):
    #     serializers=self.serializer_class(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         home=serializers.data

    #         response={
    #             "data":{
    #                 "newhome":dict(home),
    #                 "status":"Success",
    #                 "message":"New Home created successfully"
    #             }
    #         }
    #         return Response(response, status=status.HTTP_200_OK)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

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

class HomeSearch(APIView):
    serializer_class=HomeSerializer

    def get(self, request, search_term, format=None):
        homes=Home.search_by_name(search_term)
        serializers=HomeSerializer(homes, many=True)
        return Response(serializers.data)

class UserRegistration(APIView):
    serializer_class=RegistrationSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data=serializer.data

        response={
            "data":{
                "user":dict(user_data),
                "status":"Success",
                "message":"User account created successfully"
            }

        }
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self,request,format=None):
        user= User.objects.all()
        serializers=RegistrationSerializer(user, many=True)
        return Response(serializers.data)

class UserDetails(APIView):
    def get_users(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            return Http404

    def delete(self, request, pk, format=None):
        user=self.get_users(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





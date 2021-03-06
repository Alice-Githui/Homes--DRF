from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .serializers import *
from .models import *
from .models import Post as PostModel
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse, HttpResponseRedirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import FileUploadParser
from .forms import GeneralAdminRegistrationForm, ManagerRegistrationForm, HomeEntryForm, Post, HousePost, LocationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy, reverse

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

# application views
def landingpage(request):
    return render(request, 'files/landingpage.html')
    
def homepage(request):
    homes=Home.objects.all()
    location=Location.objects.all()
    # print(homes)

    return render(request, 'files/homepage.html', {"homes":homes, "locations":location})

def registration(request):
    form=GeneralAdminRegistrationForm
    if request.method == "POST":
        form=GeneralAdminRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            # return redirect('login')

    else:
        form=GeneralAdminRegistrationForm()
    return render(request, 'registration/register.html', {"form": form})

def managerRegister(request):
    form=ManagerRegistrationForm
    if request.method == "POST":
        form=ManagerRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            # return redirect('login')

    else:
        form=ManagerRegistrationForm()
    return render(request, 'registration/mregister.html', {"form": form})

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        # print(username)
        password = request.POST.get('password')
        # print(password)

        if username and password:
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('homepage')

            else:
                messages.error(request, "Username or Password is incorrect")

        else:
            messages.error(request, "Field is empty. Enter Username and Password")

    return render(request, 'registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('homepage')

@login_required(login_url="loginuser")
def newHome(request):
    form=HomeEntryForm()
    current_user=request.user
    if request.method=="POST":
        form=HomeEntryForm(request.POST, request.FILES)
        if form.is_valid():
            home=form.save(commit=False)
            home.profile=current_user
            home.save()

            return redirect('homepage')

    else:
        form=HomeEntryForm()
    return render(request, 'files/newhome.html', {"form":form})

@login_required(login_url="loginuser")
def updateHomeDetails(request, pk):
    
    home=Home.objects.get(id=pk)
    form=HomeEntryForm(instance=home)

    if request.method=="POST":
        form=HomeEntryForm(request.POST, instance=home)
        if form.is_valid():
            home=form.save(commit=False)
            # home.profile=current_user
            home.save()

            return redirect('homepage')
    
    return render(request, 'files/newhome.html', {"form":form})


def oneHome(request, pk):
    home=Home.objects.get(id=pk)

    return render(request, 'files/onehome.html', {"home":home})

def search_home(request):
    if 'homes' in request.GET and request.GET['homes']:
        location=request.GET.get('homes')
        searched_homes=Home.search_by_location(location)
        message=f"{location}"

        return render(request, 'files/lhomes.html', {"homes":searched_homes, "message":message})

    else:
        message='Please enter a house to search'
        return render(request, 'files/lhomes.html', {"message":message})

@login_required(login_url="loginuser")
def allposts(request):
    posts=PostModel.objects.all()
    
    if request.method=="POST":
        form=Post(request.POST, request.FILES)
        if form.is_valid():
            newpost=form.save(commit=False)
            newpost.save()

            # return redirect('#')

            return HttpResponseRedirect(reverse('allposts'))

    else:
        form=Post()
    return render(request, 'files/allposts.html', {"posts":posts, "form":form})

@login_required(login_url="loginuser")
def newlocation(request):
    form=LocationForm()

    if request.method=="POST":
        form=LocationForm(request.POST, request.FILES)
        if form.is_valid():
            newlocation=form.save(commit=False)
            newlocation.save()

            return redirect('homepage')

    else:
        form=LocationForm()
    return render(request, 'files/newlocation.html', {"form":form})






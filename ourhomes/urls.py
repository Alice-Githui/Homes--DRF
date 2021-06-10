from django.urls import path, include
from . import views
from rest_framework_jwt.views import refresh_jwt_token

# define paths
urlpatterns=[
    path('api/locations/', views.LocationList.as_view(), name="locations"),
    path('api/location/<int:pk>/', views.LocationDetails.as_view(), name="onelocation"),
    path('api/update/location/<int:pk>/', views.LocationDetails.as_view(), name="updatelocation"),
    path('api/delete/location/<int:pk>/', views.LocationDetails.as_view(), name="deletelocation"),
    path('api/homes/', views.HomeList.as_view(), name="homes"),
    path('api/homes/<int:pk>/', views.HomeDetails.as_view(), name="onehome"),
    path('api/homes/<str:search_term>/', views.HomeSearch.as_view(), name="homebyname"),
    path('api/update/homes/<int:pk>/', views.HomeDetails.as_view(), name="updatehome"),
    path('api/delete/homes/<int:pk>/', views.HomeDetails.as_view(), name="deletehome"),
    path('api/profileregistration/', views.UserRegistration.as_view(), name="profileregistration"),
    path('api/allusers/', views.UserRegistration.as_view(), name="allusers"),
    path('api/delete/user/<int:pk>/', views.UserDetails.as_view(), name="deleteuser"),
    path('refresh-token/', refresh_jwt_token),
    path('rest-auth/', include('rest_auth.urls')),

    path('', views.homepage, name="homepage"),
    path('registration', views.registration, name="registration"),
    path('managerRegister', views.managerRegister, name="manager-registration"),
    path('login', views.loginUser, name="loginuser"),
]
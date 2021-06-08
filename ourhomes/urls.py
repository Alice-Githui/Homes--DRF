from django.urls import path
from . import views

# define paths
urlpatterns=[
    path('api/locations/', views.LocationList.as_view(), name="locations"),
    path('api/locations/', views.LocationList.as_view(), name="postlocations"),
    path('api/onelocation/<int:pk>/', views.LocationDetails.as_view(), name="onelocation"),
    path('api/update/onelocation/<int:pk>/', views.LocationDetails.as_view(), name="updatelocation"),
    path('api/delete/location/<int:pk>/', views.LocationDetails.as_view(), name="deletelocation"),
]
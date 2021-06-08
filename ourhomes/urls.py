from django.urls import path
from . import views

# define paths
urlpatterns=[
    path('api/locations/', views.LocationList.as_view(), name="locations"),
    path('api/location/<int:pk>/', views.LocationDetails.as_view(), name="onelocation"),
    path('api/update/location/<int:pk>/', views.LocationDetails.as_view(), name="updatelocation"),
    path('api/delete/location/<int:pk>/', views.LocationDetails.as_view(), name="deletelocation"),
    path('api/homes/', views.HomeList.as_view(), name="homes"),
    path('api/homes/<int:pk>/', views.HomeDetails.as_view(), name="onehome"),
]
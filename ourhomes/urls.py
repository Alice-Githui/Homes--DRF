from django.urls import path
from . import views

# define paths
urlpatterns=[
    path('api/locations/', views.LocationList.as_view(), name="locations"),
    path('api/locations/', views.LocationList.as_view(), name="postlocations"),

]
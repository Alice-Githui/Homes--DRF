from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_homemanager=models.BooleanField(default=False)
    username=models.CharField(max_length=200, unique=True)
    first_name=models.CharField(max_length=200, unique=True)
    last_name=models.CharField(max_length=200, unique=True)
    email=models.EmailField(default="", unique=True)

 

class Home(models.Model):
    image=CloudinaryField('image')
    name=models.CharField(max_length=300)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    capacity=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class HousePost(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    home=models.ForeignKey(Home, on_delete=models.CASCADE, related_name="nameofhome")
    details=models.TextField()

    def __str__(self):
        return self.details

class Post(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    details=models.TextField()

    def __str__(self):
        return self.details







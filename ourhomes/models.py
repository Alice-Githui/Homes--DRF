from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_profile=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_homemanager=models.BooleanField(default=False)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location=models.CharField(max_length=100)
   

    def __str__(self):
        return str(self.user)

class Admin(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    designation=models.CharField(max_length=100)  

    def __str__(self):
        return str(self.user)

class HomeManager(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    designation=models.CharField(max_length=100)  
    

    def __str__(self):
        return str(self.user)

class Home(models.Model):
    image=CloudinaryField('image')
    name=models.CharField(max_length=300)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    capacity=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class HousePost(models.Model):
    name=models.ForeignKey(HomeManager, on_delete=models.CASCADE)
    home=models.ForeignKey(Home, on_delete=models.CASCADE, related_name="nameofhome")
    details=models.TextField()

    def __str__(self):
        return self.details

class Post(models.Model):
    name=models.ForeignKey(Admin, on_delete=models.CASCADE)
    details=models.TextField()

    def __str__(self):
        return self.details







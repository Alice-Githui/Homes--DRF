from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# from .models import File

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
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(default="", unique=True)

class GeneralAdmin(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

def upload_image(instance, filename):
    return "/".join(['images', str(instance.name), filename])

class Home(models.Model):
    # images=models.ImageField(blank=False, null=True, upload_to=upload_image)
    images=CloudinaryField('image', default="")
    name=models.CharField(max_length=300)
    location=models.ForeignKey(Location, on_delete=models.CASCADE, default="")
    capacity=models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def search_by_name(search_term):
        home=Home.objects.filter(name__icontains=search_term)
        return home

    def search_by_location(location):
        home=Home.objects.filter(location__name=location)
        return home

class Manager(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)


class HousePost(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    home=models.ForeignKey(Home, on_delete=models.CASCADE, related_name="nameofhome")
    details=models.TextField()

    def __str__(self):
        return str(self.name_username)

class Post(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    details=models.TextField()

    def __str__(self):
        return str(self.name_username)







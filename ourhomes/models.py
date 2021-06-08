from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Admin(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class HomeManager(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Home(models.Model):
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







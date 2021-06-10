from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms

class GeneralAdminRegistrationForm(UserCreationForm):
    # first_name=forms.CharField(required=True)
    # last_name=forms.CharField(required=True)
    # location=forms.CharField(required=True)

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email','password1', 'password2']

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_admin=True
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.save()
        generaladmin=GeneralAdmin.objects.create(user=user)
        generaladmin.location=self.cleaned_data.get('location')
        generaladmin.save()
        return user

class ManagerRegistrationForm(UserCreationForm):
    # first_name=forms.CharField(required=True)
    # last_name=forms.CharField(required=True)

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email','password1', 'password2']

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        is_homemanager=True
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.save()
        manager=Manager.objects.create(user=user)
        manager.save()
        return user

class HomeEntryForm(forms.ModelForm):
    class Meta:
        model=Home
        fields="__all__"

class Post(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"

class HousePost(forms.ModelForm):
    class Meta:
        model=HousePost
        fields="__all__"

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields="__all__"

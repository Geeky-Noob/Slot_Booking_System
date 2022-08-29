from urllib.request import Request
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
# Create your models here.

class slots(models.Model):
    username=models.CharField(max_length=100, default=None)
    bookedfor=models.TextField(default=None)

class changes(models.Model):
    sportsname=models.TextField(default=None)
    capacity=models.IntegerField()
    inventory=models.TextField()
    slots=models.IntegerField()
    courts=models.IntegerField()
    def __str__(self):
        return (self.sportsname)

class featuredMatches(models.Model):
    sportsname=models.TextField()
    eventname=models.TextField(default=None)
    eventtime=models.TextField(default=None)
    details=models.TextField()
    def __str__(self):
        return (self.eventname)
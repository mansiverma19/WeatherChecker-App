from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('password','email')
    objects = UserManager()

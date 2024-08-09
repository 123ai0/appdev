from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=150, unique=True)
    emailid = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Signup(models.Model):
    username = models.CharField(max_length=150, unique=True)
    emailid = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

class UserProfile(models.Model):
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    fat = models.FloatField()
    calories = models.FloatField()
    trainername = models.CharField(max_length=150)

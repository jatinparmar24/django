from django.db import models

# Create your models here.

class Admin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_logged_in = models.BooleanField(default=False) 

class Employee(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_logged_in = models.BooleanField(default=False)  

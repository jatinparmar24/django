from django.db import models

# Create your models here.

class Student(models.Model): 
    name = models.CharField(max_length=50) 
    age = models.IntegerField() 
    email = models.EmailField() 
    active = models.BooleanField(default=True) 
    def _str_(self): 
        return self.name

class Teacher(models.Model): 
    name = models.CharField(max_length=50) 
    contact = models.IntegerField() 
    email = models.EmailField() 
    def _str_(self): 
        return self.name
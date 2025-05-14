from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=20)
    emp_contact=models.IntegerField()
    emp_age=models.IntegerField()
    emp_email=models.EmailField(unique=True)
    emp_pass=models.CharField(max_length=20,unique=True)

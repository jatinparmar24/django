from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name     =   models.CharField(max_length=20)
    emp_contact  =   models.IntegerField()
    emp_dob      =   models.DateField()
    emp_email    =   models.EmailField(unique=True)
    emp_pass     =   models.CharField(max_length=20,unique=True)
    emp_image    =   models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return self.emp_name

  


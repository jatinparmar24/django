from django.db import models

# Create your models here.

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('MKT', 'Marketing'),
        ('OPS', 'Operations'),
    ]

    emp_name     = models.CharField(max_length=20)
    emp_contact  = models.IntegerField()
    emp_dob      = models.DateField()
    emp_email    = models.EmailField(unique=True)
    emp_pass     = models.CharField(max_length=20, unique=True)
    emp_image    = models.ImageField(upload_to='image/', null=True, blank=True)
    emp_depart   = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES,null=True)
    emp_info = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.emp_name

class NewEntry(models.Model):
    info_name    = models.CharField(max_length=50)
    info_contact = models.IntegerField()
    info_dob     = models.DateField()
    info_resume  = models.CharField(max_length=200)
    info_image   = models.ImageField(upload_to='image/', null=True, blank=True)
    admin_opinion = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.info_name

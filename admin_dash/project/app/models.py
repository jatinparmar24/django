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


class UserRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    info = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - Request"


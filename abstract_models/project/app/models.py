from django.db import models

# Create your models here.


class BaseField(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    class Meta:
        abstract=True

class Student(BaseField):
     name=models.CharField(max_length=50)
     email=models.EmailField()
     contact=None
     course=models.CharField(max_length=50)
     rollno=models.IntegerField()
     fees=models.IntegerField()

class Employee(BaseField):
     name=models.CharField(max_length=50)
     email=models.EmailField()
     contact=models.IntegerField()
     department=models.CharField(max_length=50)
     empid=models.IntegerField()
     salary=models.IntegerField()

class Cilent(BaseField):
     name=models.CharField(max_length=50)
     email=models.EmailField()
     contact=models.IntegerField()
     project=models.CharField(max_length=50)
     billing=models.IntegerField()




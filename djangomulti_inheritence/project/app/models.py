from django.db import models

# Create your models here.


class BaseField(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    

class Student(BaseField):
     
     contact=None
     course=models.CharField(max_length=50)
     rollno=models.IntegerField()
     fees=models.IntegerField()

class Employee(BaseField):
    
     department=models.CharField(max_length=50)
     empid=models.IntegerField()
     salary=models.IntegerField()

class Cilent(BaseField):
    
     project=models.CharField(max_length=50)
     billing=models.IntegerField()




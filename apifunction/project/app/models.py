from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_name=models.CharField(max_length=40)
    teacher_contact=models.IntegerField()
    teacher_age=models.IntegerField()

    def _str_(self): 
      return self.teacher_name
    
class Student(models.Model):
    student_name=models.CharField(max_length=40)
    student_contact=models.IntegerField()
    student_age=models.IntegerField()
    student_email=models.EmailField()

    def _str_(self): 
      return self.student_name


class Owner(models.Model):
    owner_name=models.CharField(max_length=40)
    owner_contact=models.IntegerField()
    owner_age=models.IntegerField()

    def _str_(self): 
      return self.owner_name

   
class Worker(models.Model):
    worker_name=models.CharField(max_length=40)
    worker_contact=models.IntegerField()
    worker_age=models.IntegerField()

    def _str_(self): 
      return self.worker_name


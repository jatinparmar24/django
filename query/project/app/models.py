from django.db import models

# Create your models here.


class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_city=models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name

    #class Meta:
      #  ordering=['stu_name']  # it gives the name on the basis of alphabet
        # to change the internal behavior of class we use Meta Class
from django.db import models

# Create your models here.

class Department(models.Model):
    depname=models.CharField(max_length=50,unique=True)
    depdis=models.CharField(max_length=200)
    dephod=models.CharField(max_length=50)

    def __str__(self):
        return str(self.depname)




class Student(models.Model):
    stuname=models.CharField(max_length=20)
    stuemail=models.EmailField()
    stucontact=models.IntegerField()
    studep=models.ForeignKey(Department,on_delete=models.PROTECT,to_field='depname',related_name='students')

    def __str__(self):
        return str(self.stuname)


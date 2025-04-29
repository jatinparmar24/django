from django.db import models

# Create your models here.


class Adhaar(models.Model):
    adharno=models.IntegerField()
    createdby=models.CharField(max_length=50)
    alloted_date=models.DateTimeField()

    def __str__(self):
        return str(self.adharno)

class Citizen(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    adharno=models.OneToOneField(Adhaar,on_delete=models.PROTECT)
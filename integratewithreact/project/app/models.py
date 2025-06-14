from django.db import models

class Registrations(models.Model):
    name = models.CharField(max_length=100)
    mode = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    age = models.IntegerField()
    contact = models.IntegerField(unique=True,blank=True)
    day = models.IntegerField(blank=True)
    person = models.IntegerField(blank= True)
    price = models.IntegerField(blank=True)
    date = models.DateField(default=True ,blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
   
    

    def __str__(self):
        return self.email

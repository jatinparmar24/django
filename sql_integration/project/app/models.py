from django.db import models

# Create your models here.

class Mydjangodatabase(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name

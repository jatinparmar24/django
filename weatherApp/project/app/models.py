from django.db import models

# Create your models here.


class Weather(models.Model):
    city=models.CharField(max_length=50)
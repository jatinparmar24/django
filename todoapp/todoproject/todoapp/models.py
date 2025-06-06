from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True , null=False)
    user_phone = models.IntegerField(unique=True)
    user_dob = models.DateField()
    user_gender = models.CharField(max_length=50)
    user_profile = models.ImageField(upload_to='image/', null=True, blank=True)
    user_pass = models.CharField(max_length=50,unique=True,null=False)

from django.db import models

# Create your models here.

quali=[(1,'B.Tech'),(2,'M.Tech')]

class UserProfile(models.Model):
    username=models.CharField(max_length=30, null=True, unique=True, db_index=True, blank=False , help_text="Enter A Unique Username")
    email=models.EmailField(max_length=255, unique=True, blank=False, db_index=True)
    bio=models.CharField(max_length=50, blank=True, null=True,db_index=True, help_text="write a Sort Bio")
    is_active=models.BooleanField(default=False, db_index=True)
    Qualification=models.CharField(max_length=100, choices=quali , null=True,verbose_name='Quali',db_index=True)




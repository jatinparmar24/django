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




class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class BaseField(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()

    class Meta:
        db_table='Student'
        # change name in db.sqlite from auth_basefield to Student
        ordering=['name']   # order of name according to name in ascending order according to ascii value
        # verbose_name="My Custom Model"  # change the name of table in admin panal    with 's' by defalut at the end
        verbose_name_plural="My Custom Model"    # it remove 's' from last


class Student(BaseField):
     
     class Meta:
        proxy=True
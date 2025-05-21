from django.db import models
from datetime import date

# question first

class Person(models.Model):
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        today = date.today()
        age= (
            today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))    
        )

        return f"you are,{age} year old."

    

class Teacher(Person):
    teacher_name = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher_name

class Student(Person):
    student_name = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name

from django.db import models
from datetime import date,timedelta
from django.utils import timezone


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


# second question

class Offer(models.Model):
    start_date=models.DateField()
    end_date=models.DateField()

    class Meta:
        abstract=True

    def is_eligible(self):
        today=date.today
        if self.start_date <= today and today <= self.end_date:
           return True
        else:
           return False


class Discount(Offer):
    d_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Discount: {self.d_name}"


class Promotion(Offer):
    p_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Promotion: {self.p_name}"



# third question 


class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class OrderedBook(Book):
    class Meta:
        proxy = True
        ordering = ['-published_date']


class FormattedBook(Book):
    class Meta:
        proxy = True

    def formatted_book_info(self):
        return f"{self.title} (Published: {self.published_date.strftime('%B %d, %Y')})"  # month,day,year


class RecentBook(Book):

    class Meta:
        proxy = True

    def get_last_year_book(self):
        one_year_ago = timezone.now().date() - timedelta(days=365)
        return self.objects.filter(published_date__gte=one_year_ago)

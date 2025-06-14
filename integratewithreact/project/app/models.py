from django.db import models

class Registrations(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    contact = models.IntegerField(unique=True, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    person = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    # Removed email and password fields

    def __str__(self):
        return self.name

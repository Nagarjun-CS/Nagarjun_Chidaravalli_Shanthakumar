from django.db import models

# Create your models here.

class Create(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)
    time = models.DateTimeField() 
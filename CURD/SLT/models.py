from django.db import models

# Create your models here.

class Details(models.Model):

    Name = models.CharField(max_length=75)
    Age = models.IntegerField()
    Cource = models.CharField(max_length=75)

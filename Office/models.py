from django.db import models
from Surgery import settings

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    height = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)


class Drug(models.Model):
    name = models.CharField(max_length=100)
    number_of_pills = models.IntegerField()
    description = models.TextField(null=True)
    gram = models.IntegerField()
    picture = models.ImageField(null=True, blank=True, upload_to='pictures/%Y/%m/%d/')


class Prescription(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    drug = models.ForeignKey('Drug', on_delete=models.CASCADE)
    date = models.DateField()

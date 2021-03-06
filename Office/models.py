from django.db import models
from Surgery import settings

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    height = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Drug(models.Model):
    name = models.CharField(max_length=100)
    number_of_pills = models.IntegerField()
    description = models.TextField(null=True)
    gram = models.IntegerField()
    picture = models.ImageField(null=True, blank=True, upload_to='pictures/%Y/%m/%d/')

    def __str__(self):
        return '{}, {}mg, {}ks'.format(self.name, self.gram, self.number_of_pills)


class Prescription(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    drug = models.ForeignKey('Drug', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return '{} {} - {}'.format(self.patient.first_name, self.patient.last_name, self.drug.name)
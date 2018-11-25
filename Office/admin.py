from django.contrib import admin
from .models import Patient, Drug, Prescription

# Register your models here.

admin.site.register(Patient)
admin.site.register(Drug)
admin.site.register(Prescription)

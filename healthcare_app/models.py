
# Create your models here.
# In healthcare_app/models.py
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    # Add more fields as needed
    class Meta:
        app_label = 'healthcare_app'

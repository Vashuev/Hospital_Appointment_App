from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

class Doctor(models.Model):
    CATEGORY = (
        ('EYE', 'EYE'),
        ('HEART', 'HEART'),
        ('GENERAL', 'GENERAL'),
        ('BRAIN', 'BRAIN')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True, choices = CATEGORY)
    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    STATUS = (
        ('DONE', 'DONE'),
        ('PENDING','PENDING')
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 200, null=True, choices=STATUS)
    def __str__(self):
        return str(self.doctor)+" "+ str(self.patient)
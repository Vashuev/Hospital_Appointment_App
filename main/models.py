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
    name = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=20, null=True, choices = CATEGORY)
    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=200, null=True)
    dob = models.DateField(max_length=50, null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    #gender = models.CharField(max_length=10, null=True)
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
    time = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length = 10, null=True, choices=STATUS)
    def __str__(self):
        return str(self.doctor)+" "+ str(self.patient)

class Prescription(models.Model):
    appoint = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine = models.CharField(max_length = 100, null=True)
    salt_name = models.CharField(max_length = 100, null=True)
    dosageperday = models.IntegerField(null=True)
    no_of_days = models.IntegerField(null=True)


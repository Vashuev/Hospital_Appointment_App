from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment, Prescription

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
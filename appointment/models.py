import datetime
from django.db import models
from patients.models import Patient
from otherusers.models import Doctor

STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('not vailable', 'Not Available'),
    ]
TIMING_CHOICES = [
    ('Morning', 'Morning'),
    ('Evening', 'Evening'),
]
class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=50, default='')
    date = models.DateField(auto_now_add=False)
    timing = models.CharField(max_length=20, choices=TIMING_CHOICES, default='morning')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    reason = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    
    def __str__(self):
        return f'{self.patient} - {self.date}'


class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    morning_available = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    evening_available = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')

    def __str__(self):
        return self.doctor.doctor_name
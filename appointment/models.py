import datetime
from django.db import models
from patients.models import Patient
from otherusers.models import Doctor

STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

TIMING_CHOICES = [
    ('Morning', 'Morning'),
    ('Evening', 'Evening'),
]
class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=50, default='')
    date = models.DateField(auto_now_add=True)
    timing = models.CharField(max_length=20, choices=TIMING_CHOICES, default='morning')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    reason = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    
    def __str__(self):
        return f'{self.patient} - {self.date}'


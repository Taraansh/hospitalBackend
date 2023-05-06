from django.db import models

# Create your models here.
AVAILABILITY_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    patient_dob = models.DateField(auto_now=False, auto_now_add=False)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=10, choices=AVAILABILITY_CHOICES)
    patient_contact = models.CharField(max_length=10)
    patient_email = models.CharField(max_length=50)
    patient_address = models.CharField(max_length=50)
    patient_password = models.CharField(max_length=50, default=123456789)

    def __str__(self):
        return self.patient_first_name + " " + self.patient_last_name
    
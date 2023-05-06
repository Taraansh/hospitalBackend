from django.db import models

# Create your models here.
AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('not available', 'Not Available'),
    ]

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=50)
    specification = models.TextField()
    doctor_email = models.CharField(max_length=50)
    doctor_password = models.CharField(max_length=50)
    morning_available = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    evening_available = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')

    def __str__(self):
        return self.doctor_name


class OtherUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    specification = models.TextField()
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
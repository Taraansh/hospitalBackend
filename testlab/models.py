from django.db import models
from patients.models import Patient

class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class PathLabTestBooking(models.Model):
    test_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='pathlab_bookings')
    test = models.CharField(max_length=50, default='')
    booking_date = models.DateField(auto_now_add=False)
    test_result_url = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=10, default='9876543210')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return f"{self.patient} - {self.test}"

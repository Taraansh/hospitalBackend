from django.db import models
from django.utils import timezone
from patients.models import Patient


class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROCESS', 'In Process'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )
    order_id = models.AutoField(primary_key=True)    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=50, default='')    
    date_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_address = models.TextField()
    contact = models.CharField(max_length=10, default='9876543210')

    def __str__(self):
        return f'Order {self.order_id} - {self.patient.patient_first_name} {self.patient.patient_last_name}'

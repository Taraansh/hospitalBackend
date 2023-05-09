from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=100, default='')
    description = models.TextField(null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.medicine_name

@receiver(post_save, sender=Medicine)
def check_quantity(sender, instance, **kwargs):
    """
    This function checks the quantity of the medicine after every save operation,
    and if the quantity is less than or equal to 10, it updates the availability
    field to False.
    """
    quantity = int(instance.quantity)
    if quantity <= 10 and instance.available:
        instance.available = False
        instance.save(update_fields=['available'])
    elif quantity > 10 and not instance.available:
        instance.available = True
        instance.save(update_fields=['available'])

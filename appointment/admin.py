from django.contrib import admin
from appointment.models import Appointment, DoctorAvailability

# Register your models here.
admin.site.register(Appointment)
admin.site.register(DoctorAvailability)
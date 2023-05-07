from rest_framework import serializers
from appointment.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        # fields = "__all__"
        fields = ('appointment_id', 'patient_name', 'doctor', 'date', 'timing', 'reason', 'total_price')

    def get_patient_name(self, obj):
        return f"{obj.patient.patient_first_name} {obj.patient.patient_last_name}"


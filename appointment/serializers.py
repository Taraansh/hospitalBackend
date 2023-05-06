from rest_framework import serializers
from appointment.models import Appointment, DoctorAvailability

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        # fields = "__all__"
        fields = ('appointment_id', 'patient_name', 'doctor', 'date', 'timing', 'status', 'reason', 'total_price')

    def get_patient_name(self, obj):
        return f"{obj.patient.patient_first_name} {obj.patient.patient_last_name}"


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()
    class Meta:
        model = DoctorAvailability
        # fields = "__all__"
        fields= ('id', 'morning_available', 'evening_available', 'doctor_name')

    def get_doctor_name(self, obj):
        return f"{obj.doctor.doctor_name}"
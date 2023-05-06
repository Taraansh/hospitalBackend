from rest_framework import serializers
from patients.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["patient_id", "patient_first_name", "patient_last_name", "patient_dob", "patient_age", "patient_gender", "patient_contact", "patient_email", "patient_address"]
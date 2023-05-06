from rest_framework import serializers
from testlab.models import Test, PathLabTestBooking

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'description', 'price']

class PathLabTestBookingSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = PathLabTestBooking
        fields = ['test_id', 'patient_name', 'test', 'booking_date', 'test_result_url', 'contact', 'total_price']

    
    def get_patient_name(self, obj):
        return f"{obj.patient.patient_first_name} {obj.patient.patient_last_name}"
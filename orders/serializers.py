from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    class Meta:
        model = Order
        # fields = "__all__"
        fields = ('order_id', 'patient_name', 'medicine_name','quantity', 'total_price', 'status', 'delivery_address', 'contact', 'date_created')

    def get_patient_name(self, obj):
        return f"{obj.patient.patient_first_name} {obj.patient.patient_last_name}"


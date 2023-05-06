from rest_framework.decorators import api_view
from rest_framework.response import Response
from patients.models import Patient
from pharmacy.models import Medicine
from .models import Order
from orders.serializers import OrderSerializer


@api_view(['POST'])
def create_order(request, patient_email):
    patient = Patient.objects.get(patient_email=patient_email)
    patient_id = patient.patient_id

    medicine_name = request.data['medicine_name']
    quantity = request.data['quantity']
    total_price = request.data['total_price']
    delivery_address = request.data['delivery_address']
    contact = request.data['contact']

    # Create a new PlaceOrder object with the provided data and associate it with the Order object
    order = Order.objects.create(patient_id=patient_id, medicine_name=medicine_name, quantity=quantity, total_price=total_price, delivery_address=delivery_address, contact=contact)
    order.save()
    serializer = OrderSerializer(order, many=False)
    return Response({"status": "success"})



@api_view(['GET'])
def view_order(request, order_id):
    order = Order.objects.get(order_id=order_id)
    serializer = OrderSerializer(order)
    return Response(serializer.data)


@api_view(['PUT'])
def update_order(request, order_id):
    order = Order.objects.get(order_id=order_id)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_order(request, order_id):
    order = Order.objects.get(order_id=order_id)
    order.delete()
    return Response({"status": "order was deleted"})


@api_view(['PUT'])
def modify_order_status(request, order_id):
    order = Order.objects.get(order_id=order_id)
    new_status = request.data.get('status')
    if new_status not in ['PENDING', 'CONFIRMED', 'SHIPPED', 'DELIVERED']:
        return Response({'error': 'Invalid order status.'})

    order.status = new_status
    order.save()
    serializer = OrderSerializer(order)
    return Response({"status": "status was updated"})


@api_view(['GET'])
def view_order_by_patient(request, patient_email):
    patient = Patient.objects.get(patient_email=patient_email)
    order = Order.objects.filter(patient=patient)
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)
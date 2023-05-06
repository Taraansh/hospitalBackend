from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pharmacy.models import Medicine
from pharmacy.serializers import MedicineSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def medicine_list(request):
    if request.method == 'GET':
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        medicine = Medicine.objects.create(
            medicine_name = request.data['medicine_name'],
            description = request.data['description'],
            quantity = request.data['quantity'],
            price = request.data['price'],
        )
        serializer = MedicineSerializer(medicine, many = False)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def medicine_detail(request, medicine_id):
    medicine = Medicine.objects.get(medicine_id=medicine_id)

    if request.method == 'GET':
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        medicine.delete()
        return JsonResponse({"status":"success"})


from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from patients.models import Patient
from testlab.models import Test, PathLabTestBooking
from testlab.serializers import TestSerializer, PathLabTestBookingSerializer

@api_view(['GET', 'POST'])
def test_list(request):
    if request.method == 'GET':
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        test = Test.objects.create(
            name = request.data['test_name'],
            description = request.data['description'],
            price = request.data['price'],
        )
        test.save()
        serializer = TestSerializer(test, many = False)
        return Response(serializer.data)


@api_view(['GET'])
def booked_tests(request):
    tests = PathLabTestBooking.objects.all()
    serializer = PathLabTestBookingSerializer(tests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def view_tests_booked_by_patient(request, patient_email):
    patient = Patient.objects.get(patient_email=patient_email)
    test = PathLabTestBooking.objects.filter(patient=patient)
    serializer = PathLabTestBookingSerializer(test, many=True)
    return Response(serializer.data)
    
    # bookings = patient.pathlab_bookings.select_related('test').all()
    # serializer = PathLabTestBookingSerializer(bookings, many=True)
    # return Response(serializer.data)

@api_view(['PUT'])
def upload_test_results(request, test_id):
    booking = PathLabTestBooking.objects.get(test_id=test_id)
    booking.test_result_url = request.data.get('test_result_url', booking.test_result_url)
    booking.save()
    serializer = PathLabTestBookingSerializer(booking, many = False)
    return Response(serializer.data)



@api_view(['POST'])
def book_test(request, patient_email):
    patient = Patient.objects.get(patient_email=patient_email)
    patient_id = patient.patient_id

    test = request.data['test']
    booking_date = request.data['booking_date']
    contact = request.data['contact']
    total_price = request.data['total_price']

    # Create a new PlaceOrder object with the provided data and associate it with the Order object
    booktest = PathLabTestBooking.objects.create(patient_id=patient_id, test=test, booking_date=booking_date, contact=contact, total_price=total_price)
    booktest.save()
    serializer = PathLabTestBookingSerializer(booktest, many=False)
    return Response({"status": "success"})


@api_view(['GET', 'PUT', 'DELETE'])
def test_detail(request, test_id):
    test = Test.objects.get(id=test_id)

    if request.method == 'GET':
        serializer = TestSerializer(test)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        test.delete()
        return JsonResponse({"status":"success"})
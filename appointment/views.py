from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from appointment.models import Appointment, DoctorAvailability
from appointment.serializers import AppointmentSerializer, DoctorAvailabilitySerializer
from patients.models import Patient


@api_view(['GET'])
def appointment_list(request, patient_email):
    patient = Patient.objects.get(patient_email=patient_email)
    appointments = Appointment.objects.filter(patient=patient)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_appointment(request, patient_email):
    patient = Patient.objects.get(patient_email=patient_email)
    patient_id = patient.patient_id

    doctor = request.data['doctor']
    date = request.data['date']
    timing = request.data['timing']
    status = request.data['status']
    reason = request.data['reason']
    total_price = request.data['total_price']

    appointment = Appointment.objects.create(patient_id=patient_id, doctor=doctor, date=date, timing=timing, status=status, reason=reason, total_price=total_price)
    appointment.save()
    serializer = AppointmentSerializer(appointment, many=False)
    return Response({"status": "success"})



@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def upcoming_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def doctor_appointments(request):
    appointments = Appointment.objects.filter(doctor=request.user)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_appointment(request):
    appointment = Appointment.objects.get(pk=request.data['id'])
    appointment.date_time = request.data['date_time']
    appointment.is_confirmed = request.data['is_confirmed']
    appointment.save()
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def doctor_availability(request):
    if request.method == 'GET':
        doctor_id = request.user.id
        # logic to retrieve doctor's availability
        return Response({'message': 'Availability retrieved successfully'})
    elif request.method == 'POST':
        doctor_id = request.user.id
        # logic to update doctor's availability
        return Response({'message': 'Availability updated successfully'})


@api_view(['GET', 'POST'])
def doctor_availability_list(request):
    if request.method == 'GET':
        availabilities = DoctorAvailability.objects.all()
        serializer = DoctorAvailabilitySerializer(availabilities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'doctor': request.user.id, **request.data}
        serializer = DoctorAvailabilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def doctor_availability_retrieve_update_destroy(request, pk):
    try:
        availability = DoctorAvailability.objects.get(pk=pk, doctor=request.user)
    except DoctorAvailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorAvailabilitySerializer(availability)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = {'doctor': request.user.id, **request.data}
        serializer = DoctorAvailabilitySerializer(availability, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        availability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
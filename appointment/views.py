from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer
from patients.models import Patient
from otherusers.models import Doctor


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
    timing = request.data['timing']
    reason = request.data['reason']
    total_price = request.data['total_price']

    appointment = Appointment.objects.create(patient_id=patient_id, doctor=doctor, timing=timing, reason=reason, total_price=total_price)
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
def upcoming_appointments(request, doctor):
    appointments = Appointment.objects.filter(doctor=doctor)
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






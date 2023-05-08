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


@api_view(['GET'])
def upcoming_appointments(request, doctor):
    appointments = Appointment.objects.filter(doctor=doctor)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)


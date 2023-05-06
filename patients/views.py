from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from patients.models import Patient
from patients.serializers import PatientSerializer
from django.http import JsonResponse

# Create your views here.
@api_view(["POST", "GET"])
def signup(request):
    # Remove this get method after completing signup process
    if request.method == "GET":
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)

    dob = request.data['patient_dob']
    dob_parts = dob.split('-')
    dob_date = date(int(dob_parts[0]), int(dob_parts[1]), int(dob_parts[2]))
    today = date.today()
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    print(dob)

    if request.method == "POST":
        patient = Patient.objects.create(
            patient_first_name = request.data['patient_first_name'],
            patient_last_name = request.data['patient_last_name'],
            patient_dob= request.data['patient_dob'],
            patient_age=age,
            patient_gender = request.data['patient_gender'],
            patient_contact = request.data['patient_contact'],
            patient_email = request.data['patient_email'],
            patient_address = request.data['patient_address'],
            patient_password = request.data['patient_password'],
        )
        patient.save()
        serializer = PatientSerializer(patient, many=False)
        return Response(serializer.data)


@api_view(["GET"])
def loginreq(request, email, password):
    if request.method == "GET":
        patient = Patient.objects.filter(patient_email = email, patient_password = password).first()
        if patient in Patient.objects.all():
            return JsonResponse({"status": "success", "email": email, "password": password })
        else:
            return JsonResponse({"status": "failed"})


@api_view(["PUT", "DELETE"])
def modify(request, email, password):
    patient = Patient.objects.get(patient_email = email, patient_password = password)

    if request.method == "PUT":
        patient.patient_first_name = request.data.get('patient_first_name', patient.patient_first_name)
        patient.patient_last_name = request.data.get('patient_last_name', patient.patient_last_name)
        patient.patient_dob = request.data.get('patient_dob', patient.patient_dob)
        patient.patient_age = request.data.get('patient_age', patient.patient_age)
        patient.patient_gender = request.data.get('patient_gender', patient.patient_gender)
        patient.patient_contact = request.data.get('patient_contact', patient.patient_contact)
        patient.patient_email = request.data.get('patient_email', patient.patient_email)
        patient.patient_address = request.data.get('patient_address', patient.patient_address)
        patient.patient_password = request.data.get('patient_password', patient.patient_password)
        patient.save()
        serializer =  PatientSerializer(patient, many = False)
        return Response(serializer.data)

    if request.method == "DELETE":
        patient.delete()
        return Response({"status":"success"})

@api_view(["GET"])
def profile(request, email, password):
    patient = Patient.objects.get(patient_email = email, patient_password = password)
    serilizer = PatientSerializer(patient, many=False)
    return Response(serilizer.data)
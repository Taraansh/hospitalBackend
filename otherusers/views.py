from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from otherusers.models import Doctor, OtherUser
from otherusers.serializers import DoctorSerializer, OtherUserSerializer
from django.db.models import Q


# Create your views here.
@api_view(["GET"])
def loginreq(request, email, password):
    if request.method == "GET":
        user = Doctor.objects.filter(doctor_email = email, doctor_password = password).first()
        if user in Doctor.objects.all():
            return JsonResponse({"status": "success", "email": email, "password": password })
        else:
            return JsonResponse({"status": "failed"})


@api_view(["PUT"])
def modify_availability(request, email, password):
    doctor = Doctor.objects.get(doctor_email = email, doctor_password = password)
    doctor.morning_available = request.data.get('morning_available', doctor.morning_available)
    doctor.evening_available = request.data.get('evening_available', doctor.evening_available)
    doctor.save()
    serializer =  DoctorSerializer(doctor, many = False)
    return Response(serializer.data)


@api_view(["GET"])
def profile(request, email, password):
    user = Doctor.objects.get(doctor_email = email, doctor_password = password)
    serilizer = DoctorSerializer(user, many=False)
    return Response(serilizer.data)

@api_view(["GET"])
def other_profile(request, email, password):
    user = OtherUser.objects.get(user_email = email, user_password = password)
    serilizer = OtherUserSerializer(user, many=False)
    return Response(serilizer.data)


@api_view(["GET"])
def doctors_list(request):
    users = Doctor.objects.all()
    serializer = DoctorSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def otheruser_login(request, email, password):
    if request.method == "GET":
        otheruser = OtherUser.objects.filter(user_email = email, user_password = password).first()
        if otheruser in OtherUser.objects.all():
            return JsonResponse({"status": "success", "email": email, "password": password, 'specification': otheruser.specification })
        else:
            return JsonResponse({"status": "failed"})
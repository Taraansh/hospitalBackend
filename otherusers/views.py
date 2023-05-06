from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from otherusers.models import Doctor, OtherUser
from otherusers.serializers import DoctorSerializer, OtherUserSerializer
from django.db.models import Q


# Create your views here.
@api_view(["GET", "POST"])
def signup(request):
    # Remove this get method after completing signup process
    if request.method == "GET":
        user = Doctor.objects.all()
        serializer = DoctorSerializer(user, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        user = Doctor.objects.create(
            user_name = request.data['user_name'],
            specification = request.data['specification'],
            user_email = request.data['user_email'],
            user_password = request.data['user_password'],
        )
        serializer = DoctorSerializer(user, many=False)
        serializer.save()
        return Response(serializer.data)
    

@api_view(["GET"])
def loginreq(request, email, password):
    if request.method == "GET":
        user = Doctor.objects.filter(user_email = email, user_password = password).first()
        if user in Doctor.objects.all():
            return JsonResponse({"status": "success", "email": email, "password": password })
        else:
            return JsonResponse({"status": "failed"})


@api_view(["PUT", "DELETE"])
def modify(request, email, password):
    user = Doctor.objects.get(user_email = email, user_password = password)

    if request.method == "PUT":
        user.user_name = request.data.get('user_name', user.user_name)
        user.specification = request.data.get('specification', user.specification)
        user.user_email = request.data.get('user_email', user.user_email)
        user.user_password = request.data.get('user_password', user.user_password)
        user.save()
        serializer =  DoctorSerializer(user, many = False)
        return Response(serializer.data)

    if request.method == "DELETE":
        user.delete()
        return Response({"status":"success"})

@api_view(["GET"])
def profile(request, email, password):
    user = Doctor.objects.get(user_email = email, user_password = password)
    serilizer = DoctorSerializer(user, many=False)
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
            return JsonResponse({"status": "success", "email": email, "password": password })
        else:
            return JsonResponse({"status": "failed"})
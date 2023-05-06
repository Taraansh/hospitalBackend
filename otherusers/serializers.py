from rest_framework import serializers
from otherusers.models import Doctor, OtherUser

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields = "__all__"

class OtherUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= OtherUser
        fields = "__all__"
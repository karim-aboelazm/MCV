from .models import *
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarDiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Diagnostic
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

class McvUserSerializer(serializers.ModelSerializer):
    class Meta:
       model = MCVUser
       fields = ['user','full_name','image','mobile']

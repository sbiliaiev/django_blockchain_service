from rest_framework import serializers

from .models import Device, DeviceData


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Device


class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DeviceData
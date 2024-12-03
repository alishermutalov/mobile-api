from rest_framework import serializers
from .models import UserDevice

class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = ['imei', 'phone_model', 'latitude', 'longitude', 'photo']

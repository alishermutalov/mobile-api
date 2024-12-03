from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserDevice
from .serializers import UserDeviceSerializer

class UserDeviceView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserDeviceSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the device info
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

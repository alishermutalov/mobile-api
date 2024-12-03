from django.urls import path
from .views import UserDeviceView

urlpatterns = [
    path('tracking/save-device-tracking/', UserDeviceView.as_view(), name='save_device_tracking'),
]

from django.db import models

class UserDevice(models.Model):
    imei = models.CharField(max_length=50, blank=True, null=True)  # IMEI or unique device ID
    phone_model = models.CharField(max_length=100)  # Phone model
    latitude = models.FloatField()  # Latitude of the device
    longitude = models.FloatField()  # Longitude of the device
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)  # User photo
    
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of record creation
    
    def __str__(self):
        return f"Device Info for {self.phone_model} - {self.imei}"

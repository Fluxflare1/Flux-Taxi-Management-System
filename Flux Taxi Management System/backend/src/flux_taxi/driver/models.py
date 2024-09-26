from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    vehicle_documents = models.FileField(upload_to='vehicle_documents/')
    is_verified = models.BooleanField(default=False)
    verification_status = models.CharField(max_length=20, default="Pending")

class Vehicle(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="Available")

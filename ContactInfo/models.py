from django.db import models

# Create your models here.
class contactinfo(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Phone_Number=models.CharField(max_length=12)
    Enquiry=models.CharField(max_length=100)
    
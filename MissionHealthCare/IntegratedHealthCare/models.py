from django.db import models

# Create your models here.
#-------------Patient Model---------------------
class patientSignUp(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=16)
    reenterpassword=models.CharField(max_length=16)

#------------Doctor Model----------------------------
class doctorSignUp(models.Model):
    name=models.CharField(max_length=200)
    specialist=models.CharField(max_length=100)
    hname=models.CharField(max_length=200)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=16)
    reenterpassword=models.CharField(max_length=16)
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
    email=models.EmailField(blank=True, null=True)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=16)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

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
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=16)

#------------Receptionist Model----------------------------
class receptionistSignUp(models.Model):
    name=models.CharField(max_length=200)
    hname=models.CharField(max_length=200)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=16)

#-------------Lab Technician Model---------------------
class labtechnicianSignUp(models.Model):
    name=models.CharField(max_length=200)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    lname=models.CharField(max_length=200)
    laddress=models.CharField(max_length=200)
    password=models.CharField(max_length=16)

#------------Admin Model----------------------------
class adminSignUp(models.Model):
    name=models.CharField(max_length=200)
    designation=models.CharField(max_length=100)
    hname=models.CharField(max_length=200)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=16)

#---------------Doctor Set Appointments-------------------
class timeSlot(models.Model):
    doctor = models.ForeignKey(doctorSignUp, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    max_appointments = models.IntegerField()
    d_price = models.IntegerField()

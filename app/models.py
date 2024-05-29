from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime    


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    F_NAME=models.CharField(max_length=50)
    L_NAME=models.CharField(max_length=50)
    STREET=models.CharField(max_length=50)
    CITY=models.CharField(max_length=50)
    STATE=models.CharField(max_length=50)
    COUNTRY=models.CharField(max_length=50)
    SPECIALIZATION=models.CharField(max_length=50)
    PHONE=models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_pic', default="{% static 'default.jped' %}")



class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    F_NAME=models.CharField(max_length=50)
    L_NAME=models.CharField(max_length=50)
    STREET=models.CharField(max_length=50)
    CITY=models.CharField(max_length=50)
    STATE=models.CharField(max_length=50)
    COUNTRY=models.CharField(max_length=50)
    DOB=models.DateField(blank=True, null=True)
    PHONE=models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_pic', default="{% static 'default.jped' %}")
    
class Drug(models.Model):
    DRUG_NAME=models.CharField(max_length=50)
    DRUG_DESCRIPTION=models.TextField()
    def __str__(self):
        return self.DRUG_NAME
    
class Appointment(models.Model):
    A_DATETIME=models.DateTimeField(default=datetime.now(), blank=True)
    D_ID=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    P_ID=models.ForeignKey(Patient, on_delete=models.CASCADE)
    is_complete=models.BooleanField(default=False)


    

class LabTest(models.Model):
    TEST_NAME=models.CharField(max_length=50)
    TEST_DESCRIPTION=models.TextField()
    def __str__(self):
        return self.TEST_NAME

class Treatment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    T_Desc=models.TextField()
    Drug=models.ManyToManyField(Drug)
    LabTest=models.ManyToManyField(LabTest)




    


from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Patient,Doctor,User

UserModel = get_user_model()  # Use your custom model if applicable

class PatientSignupForm(UserCreationForm):
    F_NAME=forms.CharField(max_length=50)
    L_NAME=forms.CharField(max_length=50)
    CITY=forms.CharField(max_length=50)
    STATE=forms.CharField(max_length=50)
    COUNTRY=forms.CharField(max_length=50)
    STREET=forms.CharField(max_length=50)
    PHONE=forms.CharField(max_length=20)
    DOB=forms.DateField()
    image = forms.ImageField(required=False)

    class Meta:
        model = User  # Update if using a custom User model
        
        fields = ('username', 'email', 'F_NAME', 'L_NAME', 'STREET', 'CITY', 'STATE', 'COUNTRY',  'DOB','PHONE','image', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Access student-specific fields here
        user.is_patient = True
        user.save()
        patient=Patient.objects.create(user=user)
        patient.F_NAME=self.cleaned_data['F_NAME']
        patient.L_NAME=self.cleaned_data['L_NAME']
        patient.CITY=self.cleaned_data['CITY']
        patient.STATE=self.cleaned_data['STATE']
        patient.COUNTRY=self.cleaned_data['COUNTRY']
        patient.STREET=self.cleaned_data['STREET']
        patient.DOB=self.cleaned_data['DOB']
        patient.PHONE=self.cleaned_data['PHONE']
        patient.image=self.cleaned_data['image']
        patient.save()
        return user

class DoctorSignupForm(UserCreationForm):
    F_NAME=forms.CharField(max_length=50)
    L_NAME=forms.CharField(max_length=50)
    CITY=forms.CharField(max_length=50)
    STATE=forms.CharField(max_length=50)
    COUNTRY=forms.CharField(max_length=50)
    STREET=forms.CharField(max_length=50)
    PHONE=forms.CharField(max_length=20)
    image = forms.ImageField(required=False)
    SPECIALIZATION=forms.CharField(max_length=50)

    class Meta:
        model = User  # Update if using a custom User model
        fields = ('username', 'email', 'F_NAME', 'L_NAME', 'STREET', 'CITY', 'STATE', 'COUNTRY',  'SPECIALIZATION','PHONE','image', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Access student-specific fields here
        user.is_doctor = True
        user.save()
        doctor=Doctor.objects.create(user=user)
        doctor.F_NAME=self.cleaned_data['F_NAME']
        doctor.L_NAME=self.cleaned_data['L_NAME']
        doctor.CITY=self.cleaned_data['CITY']
        doctor.STATE=self.cleaned_data['STATE']
        doctor.COUNTRY=self.cleaned_data['COUNTRY']
        doctor.STREET=self.cleaned_data['STREET']
        doctor.SPECIALIZATION=self.cleaned_data['SPECIALIZATION']
        doctor.PHONE=self.cleaned_data['PHONE']
        doctor.image=self.cleaned_data['image']
        doctor.save()
        return user

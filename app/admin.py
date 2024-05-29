from django.contrib import admin
from .models import Doctor,Patient,Appointment,User,Treatment,Drug,LabTest
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(User)
admin.site.register(Treatment)
admin.site.register(Drug)
admin.site.register(LabTest)
# Register your models here.

"""
URL configuration for hospitalmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),path("",views.home,name='home'),
    path('doctor/signup',views.DoctorSignupView.as_view(),name='Doctorsignup'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.hh,name='logout'),
    path('patient/signup',views.PatientSignupView.as_view(),name='Patientsignup'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('addappointment',views.create_appointment,name='addappointment'),
    path('<int:pk>/treatment/create',views.CreateTreatment.as_view(), name='create_treatment'),
    path('appointment/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
]

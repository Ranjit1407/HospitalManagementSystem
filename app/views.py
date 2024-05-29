
from django.forms import BaseModelForm

from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import CreateView,UpdateView,DetailView
from.forms import PatientSignupForm,DoctorSignupForm
from .models import User
from django.contrib.auth.decorators import login_required
from .models import Patient,Doctor,User,Appointment,Treatment

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:  # Show all appointments for superuser
            appointments = Appointment.objects.all()
        else:
            if(request.user.is_doctor):
                appointments = Appointment.objects.filter(D_ID=request.user.doctor)
            else:
                appointments = Appointment.objects.filter(P_ID=request.user.patient) # Get first 3 appointments for the user
        upcoming=[]
        past=[]
        for i in appointments:
            if(i.is_complete):
                past.append(i)
            else:
                upcoming.append(i)
        
        context = {'upcoming_appointments': upcoming,'past_appointments': past}
        print(context)
    else:
        context = {}
    return render(request, 'app/home.html', context)

def hh(request):
    logout(request)
    return render(request,'app/home.html')

def profile(request):
    user = request.user
    return render(request, 'app/profile.html', {'user': user})


@login_required
def create_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        patient_id = request.POST.get('patient')
        date_time = request.POST.get('date_time')
        # Validate and sanitize user input

        doctor = Doctor.objects.get(F_NAME=doctor_id)
        patient = Patient.objects.get(F_NAME=patient_id)

        appointment = Appointment.objects.create(
            D_ID=doctor,
            P_ID=patient,
            A_DATETIME=date_time
        )
        return redirect('home')  # Redirect to appointment list (optional)
    else:
        doctors = Doctor.objects.all()
        patients = Patient.objects.all()
        context = {'doctors': doctors, 'patients': patients}
        return render(request, 'app/create_appointment.html', context)

class DoctorSignupView(CreateView):
    form_class = DoctorSignupForm
    template_name = 'app/signup.html'  # Adjust template name
    model=User
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class PatientSignupView(CreateView):
    form_class = PatientSignupForm
    template_name = 'app/signup.html'  # Adjust template name
    model=User
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class CreateTreatment(CreateView):
    model=Treatment
    fields=['T_Desc','Drug','LabTest']
    template_name='app/create_treatment.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form: BaseModelForm):
        appointment_id = self.kwargs.get('pk')
        appointment = get_object_or_404(Appointment, pk=appointment_id)
        appointment.is_complete=True
        appointment.save()
        form.instance.appointment=appointment
        return super().form_valid(form)
    def form_invalid(self, form):
        print('form_invalid')


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'app/appointment_detail.html'




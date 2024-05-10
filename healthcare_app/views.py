
# Create your views here.
# In healthcare_app/views.py
# from django.shortcuts import render, redirect
# from .forms import PatientForm

# def add_patient(request):
#     if request.method == 'POST':
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('patient_list')  # Redirect to patient list page
#     else:
#         form = PatientForm()
#     return render(request, 'add_patient.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import PatientForm

from .models import Patient

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome_message')  # Redirect to welcome message page
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

def welcome_message(request):
    return render(request, 'welcome_message.html')


def patient_list(request):
    patients = Patient.objects.all()  # Retrieve all patients from the database
    return render(request, 'patient_list.html', {'patients': patients})


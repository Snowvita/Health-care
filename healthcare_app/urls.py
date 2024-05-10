# your_app/urls.py
from django.urls import path
from .views import add_patient,welcome_message,patient_list

urlpatterns = [
    path('', add_patient, name='add_patient'),
     path('welcome/', welcome_message, name='welcome_message'),
         path('patient-list/', patient_list, name='patient_list'),

]

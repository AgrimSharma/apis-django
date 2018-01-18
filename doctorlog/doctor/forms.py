# coding=utf-8
import django.forms
from suit.widgets import AutosizedTextarea, SuitSplitDateTimeWidget, HTML5Input, EnclosedInput
from .models import DoctorPatient, Doctor, DoctorAppointment, Medication


class DoctorForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', "email", 'password', 'role',
                  'status', "createdDate", "updatedDate"]
        widgets = {
            "first_name": AutosizedTextarea,
            "email": EnclosedInput(append='icon-envelope'),
            "last_name": AutosizedTextarea,
            "password": HTML5Input(input_type='password'),
            'createdDate': SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget
        }


class DoctorPatientForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = DoctorPatient
        fields = ['doctor', 'patient', 'status', "createdDate", "updatedDate"]
        widgets = {
            'createdDate': SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget
        }


class DoctorAppointmentForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = DoctorAppointment
        fields = ['doctor', 'patient', 'appointmentDate','status', "createdDate", "updatedDate"]
        widgets = {
            'appointmentDate': SuitSplitDateTimeWidget,
            'createdDate': SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget
        }


class MedicationForm(django.forms.ModelForm):
    """
    User form
    """
    medicine_pic = django.forms.ImageField,

    class Meta:
        model = Medication
        fields = ['name', 'prescribed_by', 'patient', 'dose', "medicine_pic",
                  "schedule", "medicine_type", "instructions", "remind_me", "refills",
                  "boxters"]

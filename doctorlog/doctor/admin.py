from django.contrib import admin
from .models import Doctor, DoctorPatient, DoctorAppointment
from .forms import DoctorForm, DoctorPatientForm, DoctorAppointmentForm
# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    """
    User Admin Panel
    """
    form = DoctorForm
    list_display = ('first_name', 'last_name', 'role')
    fields = [('first_name', 'last_name'), 'password', 'role', "email",
              'createdDate', 'updatedDate', 'status']


class DoctorPatientAdmin(admin.ModelAdmin):
    """
    User Admin Panel
    """
    form = DoctorPatientForm
    list_display = ('doctors', "patients")
    fields = ["doctor", "patient", 'createdDate', 'updatedDate', 'status']

    def patients(self, obj):
        return ", ".join([p.get_full_name() for p in obj.patient.all()])

    def doctors(self, obj):
        return obj.doctor.get_full_name()


class DoctorPatientAppointmentAdmin(admin.ModelAdmin):
    """
    User Admin Panel
    """
    form = DoctorAppointmentForm
    list_display = ('doctors', 'patients', "appointmentDate")
    fields = ["doctor", "patient", 'appointmentDate', 'createdDate', 'updatedDate', 'status']

    def patients(self, obj):
        return obj.patient.get_full_name()

    def doctors(self, obj):
        return obj.doctor.get_full_name()

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorPatient, DoctorPatientAdmin)
admin.site.register(DoctorAppointment, DoctorPatientAppointmentAdmin)

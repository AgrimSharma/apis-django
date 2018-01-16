from .serializers import DoctorSerializer, DoctorPatientSerializer, DoctorAppointmentSerializer, MedicationSerializer
from .models import Doctor, DoctorPatient, DoctorAppointment, Medication
from rest_framework import viewsets


class DoctorViewSet(viewsets.ModelViewSet):
    """<h4>API endpoint that allows users to be viewed or edited.</h4>"""

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorPatientViewSet(viewsets.ModelViewSet):
    """<h4>API endpoint that allows users to be viewed or edited.</h4>"""

    queryset = DoctorPatient.objects.all()
    serializer_class = DoctorPatientSerializer


class DoctorAppointmentViewSet(viewsets.ModelViewSet):
    """<h4>API endpoint that allows users to be viewed or edited.</h4>"""

    queryset = DoctorAppointment.objects.all()
    serializer_class = DoctorAppointmentSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    """<h4>API endpoint that allows users to be viewed or edited.</h4>"""

    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

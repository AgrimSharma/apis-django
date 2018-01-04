from .serializers import DoctorSerializer, DoctorPatientSerializer
from .models import Doctor, DoctorPatient
from rest_framework import viewsets


class DoctorViewSet(viewsets.ModelViewSet):
    """<h4>API endpoint that allows users to be viewed or edited.</h4>"""

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorPatientViewSet(viewsets.ModelViewSet):
    """<h4>API endpoint that allows users to be viewed or edited.</h4>"""

    queryset = DoctorPatient.objects.all()
    serializer_class = DoctorPatientSerializer

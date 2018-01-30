from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from doctorbox_web.api.models import Medication, Doctor, ArticleCategory, \
    Symptom, Prescription, LoggedSymptom, Vital
from doctorbox_web.api.serializers import ArticleCategorySerializer, \
    ArticleSerializer, MedicationSerializer, DosageSerializer, \
    DoctorSerializer, SymptomSerializer, ReadPrescriptionSerializer,\
    WritePrescriptionSerializer, LoggedSymptomSerializer, VitalSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all().order_by('name')
    serializer_class = MedicationSerializer

    @detail_route()
    def dosages(self, request, pk=None):
        medication = self.get_object()
        serializer = DosageSerializer(medication.dosages.all(), context={'request': request}, many=True)

        return Response(serializer.data)


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()

    def get_serializer_class(self):
        if 'POST' == self.request.method:
            return WritePrescriptionSerializer
        return ReadPrescriptionSerializer

    def create(self, request, *args, **kwargs):
        if hasattr(request, 'patient'):
            serializer = WritePrescriptionSerializer(context={'request': request}, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        if hasattr(request, 'patient'):
            patient = request.patient
            if request.method == 'GET':
                prescriptions = Prescription.objects.filter(patient=patient)
                serializer = ReadPrescriptionSerializer(prescriptions,
                                                        context={'request': request},
                                                        many=True)
                return Response(serializer.data)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class SymptomViewSet(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer


class ArticleCategoryViewSet(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all().order_by('order')
    serializer_class = ArticleCategorySerializer

    @detail_route()
    def articles(self, request, pk=None):
        article_category = self.get_object()
        serializer = ArticleSerializer(article_category.articles.all(), context={'request': request}, many=True)

        return Response(serializer.data)


class LoggedSymptomViewSet(viewsets.ModelViewSet):
    queryset = LoggedSymptom.objects.all()
    serializer_class = LoggedSymptomSerializer


class VitalViewSet(viewsets.ModelViewSet):
    queryset = Vital.objects.all()
    serializer_class = VitalSerializer

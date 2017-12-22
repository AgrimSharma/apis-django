"""# coding=utf-8."""
from .models import VitalReport, Vitals
from .serializers import VitalsReportSerializer, VitalsSerializer, \
    VitalByName, VitalRecordUserList
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework import status
from modules.serializers import UserSerializerReport
from rest_framework.generics import GenericAPIView


class VitalsAPI(viewsets.ModelViewSet):
    """<h4>API endpoint that allows users to be viewed or edited.</h4>."""

    queryset = Vitals.objects.all()
    serializer_class = VitalsSerializer


class VitalsReportAPI(viewsets.ModelViewSet):
    """<h4>API endpoint allows users to view or edit Vital Reports.</h4>."""

    queryset = VitalReport.objects.all()
    serializer_class = VitalsReportSerializer


class VitalsNameAPI(GenericAPIView):
    """<h4>List vitals by name</h4>."""

    queryset = Vitals.objects.all()
    serializer_class = VitalByName

    def post(self, request):
        """<h4>List vitals by name</h4>."""
        vitals = Vitals.objects.filter(name__icontains=request.data['name'])
        result = []
        for r in vitals:
            result.append(VitalsSerializer(r).data)
        return JsonResponse(dict(response=result, status=status.HTTP_200_OK))


class VitalsReportUserAPI(GenericAPIView):
    """<h4>List Vitals Report by user ID</h4>."""

    queryset = VitalReport.objects.all()
    serializer_class = VitalRecordUserList

    def post(self, request):
        """<h4>List Vitals Report by user ID</h4>."""
        response = []
        vitals_report = VitalReport.objects.filter(
            userID__id=request.data['userID'])
        for i, v in enumerate(vitals_report):
            resp = VitalsReportSerializer(v).data
            vitals = VitalsSerializer(v.vitalID).data
            user = UserSerializerReport(v.userID).data
            response.append(dict(user=user, vitals=vitals, vitals_report=resp,
                                 vitals_report_id=v.id))
        return JsonResponse(dict(response=response, status=status.HTTP_200_OK))

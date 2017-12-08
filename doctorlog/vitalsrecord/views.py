# coding=utf-8
from .models import *
from .serializers import VitalsReportSerializer, VitalsSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from modules.models import Users
from modules.serializers import UserSerializer


class VitalsAPI(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vitals.objects.all()
    serializer_class = VitalsSerializer


class VitalsReportAPI(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VitalReport.objects.all()
    serializer_class = VitalsReportSerializer


class VitalsNameAPI(APIView):
    """
    List vitals by name
    """
    def get(self, request, name):
        """
        List vitals by name
        """
        vitals = Vitals.objects.filter(name__icontains=name.replace("%20", " "))
        result = []
        for r in vitals:
            result.append(VitalsSerializer(r).data)
        return JsonResponse(dict(response=result, status=status.HTTP_200_OK))


class VitalsReportUserAPI(APIView):
    """
    List Vitals Report by user ID
    """
    def get(self, request, user_id):
        """
        List Vitals Report by user ID
        """
        if user_id:
            response = []
            vitals_report = VitalReport.objects.filter(userID__id=user_id, status=True)
            for i,v in enumerate(vitals_report):
                resp = VitalsReportSerializer(v).data
                vitals = VitalsSerializer(Vitals.objects.get(id=resp.get('vitalID'))).data
                user = UserSerializer(Users.objects.get(id=resp.get('userID'))).data
                response.append(dict(user=user, vitals=vitals, vitals_report=resp, vitals_report_id=v.id))
            return JsonResponse(dict(response=response, status=status.HTTP_200_OK))
        else:
            return JsonResponse(dict(response='Vitals Report not Found', status=status.HTTP_404_NOT_FOUND))

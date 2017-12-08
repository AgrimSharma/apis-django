# coding=utf-8
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from .models import SymptomsDef, SymptomsRecord, SymptomsUser
from .serializers import SymptomsRecordSerializer, SymptomsUserSerializer, SymptomsDefSerializer
from rest_framework import viewsets
from rest_framework import status
from modules.serializers import UserSerializer
from modules.models import Users


class SymptomsListAPI(viewsets.ModelViewSet):
    """
    SymptomsList API endpoint that allows symptoms to be viewed or edited.
    """
    queryset = SymptomsUser.objects.all()
    serializer_class = SymptomsUserSerializer


class SymptomsAPI(viewsets.ModelViewSet):
    """
    SymptomsAPI endpoint that allows symptoms to be viewed or edited.
    """
    queryset = SymptomsDef.objects.all()
    serializer_class = SymptomsDefSerializer


class SymptomsRecordsAPI(viewsets.ModelViewSet):
    """
    SymptomsRecord API endpoint that allows symptoms records to be viewed or edited.
    """
    queryset = SymptomsRecord.objects.all()
    serializer_class = SymptomsRecordSerializer


class SymptomsListUserAPI(APIView):
    """
    List Symptoms by user ID
    """
    def get(self, request, user_id):
        """
        List Symptoms by user ID
        """
        if user_id:
            symptoms = SymptomsUser.objects.filter(userID__id=user_id)
            response = []
            for s in symptoms:
                resp = SymptomsUserSerializer(s).data
                user = UserSerializer(Users.objects.get(id=resp.get("userID"))).data
                response.append(dict(user=user, symptoms_user=SymptomsUserSerializer(s).data, symptoms_user_id=s.id))
            return JsonResponse(dict(response=response, status=status.HTTP_200_OK))
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


class SymptomsRecordsUserAPI(APIView):
    """
    List Symptoms Records By user ID
    """
    def get(self, request, user_id):
        """
        List Symptoms Records By user ID
        """
        if user_id:
            values = SymptomsRecord.objects.filter(userID__id=user_id, status=True)
            result = []
            for x in values:
                symptoms_record = SymptomsRecordSerializer(x).data
                user = UserSerializer(Users.objects.get(id=symptoms_record.get('userID'))).data
                symptoms = SymptomsUserSerializer(SymptomsUser.objects.get(id=symptoms_record.get('symptomsID'))).data
                result.append(dict(user=user, symptoms=symptoms, symptoms_record=symptoms_record,
                                   symptoms_record_id=x.id))
            return JsonResponse(dict(response=result, status=status.HTTP_200_OK))
        else:
            return JsonResponse(dict(response="Not Found", status=status.HTTP_404_NOT_FOUND))


class SymptomsDefAPI(APIView):
    """
    Symptoms Def API
    """
    def get(self, request, name):
        """
        Symptoms Def API
        """
        if name:
            symptoms_def = SymptomsDef.objects.filter(name__contains=name)
            result = []
            for x in symptoms_def:
                result.append(SymptomsDefSerializer(x).data)
            return JsonResponse(dict(response=result, status=status.HTTP_200_OK))
        else:
            return JsonResponse(dict(response="Not Found", status=status.HTTP_404_NOT_FOUND))


"""# coding=utf-8."""
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from .models import SymptomsDef, SymptomsRecord, SymptomsUser
from .serializers import SymptomsRecordSerializer, SymptomsUserSerializer, \
    SymptomsDefSerializer, SymptomsRecordUser, SymptomsUserList, SymptomsByName
from rest_framework import viewsets
from rest_framework import status
from modules.serializers import UserSerializerReport


class SymptomsListAPI(viewsets.ModelViewSet):
    """<h4>SymptomsList API that allows symptoms be viewed or edited</h4>."""

    queryset = SymptomsUser.objects.all()
    serializer_class = SymptomsUserSerializer


class SymptomsAPI(viewsets.ModelViewSet):
    """<h4>SymptomsAPI that allows symptoms to be viewed or edited<h4>."""

    queryset = SymptomsDef.objects.all()
    serializer_class = SymptomsDefSerializer


class SymptomsRecordsAPI(viewsets.ModelViewSet):
    """<h4>API endpoint allows symptoms records to be viewed or edited</h4>."""

    queryset = SymptomsRecord.objects.all()
    serializer_class = SymptomsRecordSerializer


class SymptomsRecordsUserAPI(GenericAPIView):
    """<h4>List Symptoms Records By user ID</h4>."""

    queryset = SymptomsRecord.objects.all()
    serializer_class = SymptomsRecordUser

    def post(self, request):
        """<h4>List Symptoms Records By user ID</h4>."""
        user = SymptomsRecord.objects.filter(userID__id=request.data['userID'],
                                             status=True)
        result = []
        for x in user:
            symptoms_record = SymptomsRecordSerializer(x).data
            user = UserSerializerReport(x.userID).data
            symptoms = SymptomsUserSerializer(x.symptomsID).data
            result.append(dict(user=user, symptoms=symptoms,
                               symptoms_record=symptoms_record,
                               symptoms_record_id=x.id))
        return JsonResponse(dict(response=result, status=status.HTTP_200_OK))


class SymptomsListUserAPI(GenericAPIView):
    """<h4>List Symptoms by user ID</h4>."""

    queryset = SymptomsRecord.objects.all()
    serializer_class = SymptomsUserList

    def post(self, request):
        """<h4>List Symptoms by user ID</h4>."""
        symptoms = SymptomsUser.objects.filter(
            userID__id=request.data['userID'])
        response = []
        for s in symptoms:
            user = UserSerializerReport(s.userID).data
            response.append(
                dict(user=user, symptoms_user=SymptomsUserSerializer(s).data,
                     symptoms_user_id=s.id))
        return JsonResponse(dict(response=response, status=status.HTTP_200_OK))


class SymptomsDefName(GenericAPIView):
    """<h4>User Verification API</h4>."""

    queryset = SymptomsDef.objects.all()
    serializer_class = SymptomsByName

    def post(self, request):
        """<h4>validate a user by email</h4>."""
        symptom = SymptomsDef.objects.get(name__icontains=request.data['name'])
        return JsonResponse(dict(name=symptom.name,
                                 subTitle=symptom.subTitle,
                                 description=symptom.description,
                                 mediaTitle=symptom.mediaTitle,
                                 mediaURL=symptom.mediaURL,
                                 describe=symptom.describe,
                                 location=symptom.location,
                                 length=symptom.length,
                                 triggeredBy=symptom.triggeredBy,
                                 otherSymptoms=symptom.otherSymptoms,
                                 reliefBy=symptom.reliefBy,
                                 createdDate=symptom.createdDate,
                                 updatedDate=symptom.updatedDate,
                                 status=symptom.status
                                 ))

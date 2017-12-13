# coding=utf-8
from django.http import JsonResponse
from rest_framework.views import APIView

from .models import *
from rest_framework import status
from rest_framework import viewsets
from .serializers import UserSerializer
from .utils import check_disease


class Ping(APIView):
    """
    Test method to check api functioning
    """
    def get(self, request):
        return JsonResponse(dict(response='pong', status=status.HTTP_200_OK))


class SymptomsList(APIView):
    """
    Test method to check api functioning
    """
    def get(self, request, disease):
        return JsonResponse(dict(response=check_disease(disease.lower()), status=status.HTTP_200_OK))


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserByEmailAPI(APIView):
    """
    Test method to check api functioning
    """
    def get(self, request, email):
        user = Users.objects.get(email=email)
        user_serialized = UserSerializer(user).data
        return JsonResponse(dict(response=user_serialized, status=status.HTTP_200_OK))


class LoginUserAPI(APIView):
    """
    User Verification API
    """
    def post(self,request, email, password):
        try:
            user = Users.objects.get(email=email)
            check = user.check_password(password)
            if check:
                return JsonResponse(dict(name=user.get_full_name(), role= user.role, status=status.HTTP_200_OK))
            else:
                return JsonResponse(dict(status=status.HTTP_404_NOT_FOUND))
        except Exception:
            return JsonResponse(dict(status=status.HTTP_404_NOT_FOUND))



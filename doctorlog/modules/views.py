# coding=utf-8
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .models import *
from rest_framework import status
from rest_framework import viewsets
from .serializers import UserSerializer, Authentication, UserByEmail


class Ping(APIView):
    """
    <h4>Test method to check api functioning</h4>
    """
    def get(self, request):
        return JsonResponse(dict(response='pong', status=status.HTTP_200_OK))


class UserViewSet(viewsets.ModelViewSet):
    """
    <h4>API endpoint that allows users to be viewed or edited.</h4>
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserByEmailAPI(GenericAPIView):
    """
    Test method to check api functioning
    """
    queryset=User.objects.all()
    serializer_class= UserByEmail

    def post(self, request):
        """
        <h4>List as user by email id</h4>
        """

        user = User.objects.get(email=request.data['email'])
        user_serialized = UserSerializer(user).data
        return JsonResponse(dict(response=user_serialized, status=status.HTTP_200_OK))


class LoginUserAPI(GenericAPIView):
    """
    <h4>User Verification API<h4>
    """
    queryset=User.objects.all()
    serializer_class=Authentication

    def post(self, request):
        """
        <h4>validate a user by email</h4>
        """
        user = User.objects.get(email=request.data['email'])
        check = check_password(request.data['password'], user.password)
        return JsonResponse(dict(status=status.HTTP_200_OK) if check else dict(status=status.HTTP_404_NOT_FOUND))


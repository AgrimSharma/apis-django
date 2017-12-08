# coding=utf-8

from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('firstName', 'lastName', 'email', 'role')

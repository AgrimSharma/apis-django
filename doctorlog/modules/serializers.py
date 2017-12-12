# coding=utf-8

from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    User Serialization
    """
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Users
        fields = ('firstName', 'lastName', 'email','password','role','updatedDate')


class UserSerializerReport(serializers.ModelSerializer):
    """
    User Serialization without password
    """
    class Meta:
        model = Users
        fields = ('firstName', 'lastName', 'email','role','updatedDate')

# coding=utf-8

from .models import *
from rest_framework import serializers
import datetime

class UserSerializer(serializers.ModelSerializer):
    """
    User Serialization
    """
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    createdDate = serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate = serializers.DateTimeField(default=datetime.datetime.now())
    class Meta:
        model = Users
        fields = ('firstName', 'lastName', 'email','password','role',"createdDate",'updatedDate')


class UserSerializerReport(serializers.ModelSerializer):
    """
    User Serialization without password
    """
    class Meta:
        model = Users
        fields = ('firstName', 'lastName', 'email','role','updatedDate')

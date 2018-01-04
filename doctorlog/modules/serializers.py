# coding=utf-8

from .models import *
from rest_framework import serializers
import datetime


class UserSerializer(serializers.ModelSerializer):
    """
    User Serialization
    """
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)
    createdDate = serializers.DateTimeField(
        default=datetime.datetime.now())
    updatedDate = serializers.DateTimeField(
        default=datetime.datetime.now())

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'password', 'role',
                  "createdDate", 'updatedDate')


class UserSerializerReport(serializers.ModelSerializer):
    """
    User Serialization without password
    """
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'role', 'updatedDate')


class Authentication(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    email=serializers.EmailField(write_only=True)

    class Meta:
        model=User
        fields=('email', 'password')


class UserByEmail(serializers.ModelSerializer):
    email=serializers.EmailField(write_only=True)

    class Meta:
        model=User
        fields=('email',)
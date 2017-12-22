# coding=utf-8
"""serializer."""
from .models import Users
from rest_framework import serializers
import datetime


class UserSerializer(serializers.ModelSerializer):
    """User Serialization."""

    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)
    createdDate = serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate = serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        """Meta class."""

        model = Users
        fields = ('first_name', 'last_name', 'email', 'password', 'role',
                  "createdDate", 'updatedDate')


class UserSerializerReport(serializers.ModelSerializer):
    """User Serialization without password."""

    class Meta:
        """Meta class."""

        model = Users
        fields = ('first_name', 'last_name', 'email', 'role', 'updatedDate')


class Authentication(serializers.ModelSerializer):
    """Authentication Serializer."""

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        """Meta."""

        model = Users
        fields = ('email', 'password')


class UserByEmail(serializers.ModelSerializer):
    """User By Email Serializer."""

    email = serializers.EmailField(write_only=True)

    class Meta:
        """Meta."""

        model = Users
        fields = ('email',)

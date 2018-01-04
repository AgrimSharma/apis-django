# coding=utf-8

from .models import DoctorAppointment, DoctorPatient, Doctor
from rest_framework import serializers
import datetime


class DoctorSerializer(serializers.ModelSerializer):
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
        model = Doctor
        fields = ('first_name', 'last_name', 'email', 'password', 'role',
                  "createdDate", 'updatedDate')


class DoctorPatientSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(
        default=datetime.datetime.now())
    updatedDate = serializers.DateTimeField(
        default=datetime.datetime.now())

    class Meta:
        model = DoctorPatient
        fields = ("doctor", "patient", "createdDate", 'updatedDate')

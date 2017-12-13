# coding=utf-8
from rest_framework import serializers
from .models import *
import datetime

class VitalsSerializer(serializers.ModelSerializer):
    """
    Vital Serializer to serialize data from models
    """
    createdDate = serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate = serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        model = Vitals
        fields = ('name', 'description',"mediaTitle","mediaURL",'options', 'info', 'tips',
                  "updatedDate", "createdDate")


class VitalsReportSerializer(serializers.ModelSerializer):
    """
    Vital Reports Serializer to serialize data from models
    """
    createdDate=serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate=serializers.DateTimeField(default=datetime.datetime.now())
    reportedDate=serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        model = VitalReport
        fields = ('weight', 'systol', 'dystol',"heartRate", "options", "temperature",
                  "pulse","sugar", "stressLevel", "comment", "reportedDate", "updatedDate", "createdDate")

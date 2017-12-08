# coding=utf-8
from rest_framework import serializers
from .models import *


class VitalsSerializer(serializers.ModelSerializer):
    """
    Vital Serializer to serialize data from models
    """
    class Meta:
        model = Vitals
        fields = ('name', 'description',"mediaTitle","mediaURL",'options', 'info', 'tips',
                  "updatedDate")


class VitalsReportSerializer(serializers.ModelSerializer):
    """
    Vital Reports Serializer to serialize data from models
    """
    class Meta:
        model = VitalReport
        fields = ('weight', 'systol', 'dystol',"heartRate", "options", "temperature",
                  "pulse","sugar", "stressLevel", "comment", "reportedDate", "updatedDate")

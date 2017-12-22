"""# coding=utf-8."""
from rest_framework import serializers
from .models import VitalReport, Vitals
import datetime


class VitalsSerializer(serializers.ModelSerializer):
    """Vital Serializer to serialize data from models."""

    createdDate = serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate = serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        """Meta."""

        model = Vitals
        fields = ('name', 'description', "mediaTitle", "mediaURL", 'options',
                  'info', 'tips', "updatedDate", "createdDate")


class VitalsReportSerializer(serializers.ModelSerializer):
    """Vital Reports Serializer to serialize data from models."""

    createdDate = serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate = serializers.DateTimeField(default=datetime.datetime.now())
    reportedDate = serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        """Meta."""

        model = VitalReport
        fields = ('weight', 'systol', 'dystol', "heartRate", "options",
                  "temperature", "pulse", "sugar", "stressLevel",
                  "comment", "reportedDate", "updatedDate", "createdDate")


class VitalRecordUserList(serializers.ModelSerializer):
    """Serializer Symptoms Record."""

    userID = serializers.CharField()

    class Meta:
        """Meta."""

        model = VitalReport
        fields = ('userID',)


class VitalByName(serializers.ModelSerializer):
    """Serializer Symptoms Record."""

    name = serializers.CharField()

    class Meta:
        """Meta."""

        model = Vitals
        fields = ('name',)

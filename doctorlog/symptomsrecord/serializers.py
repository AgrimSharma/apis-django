# coding=utf-8
from rest_framework import serializers
from .models import *
import datetime

class SymptomsUserSerializer(serializers.ModelSerializer):
    """
    Serializer Symptoms User
    """
    createdDate = serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate = serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        model = SymptomsUser
        fields = ('userID', 'name', 'subTitle', 'description','describe', 'location', 'length',
                  'triggeredBy', "otherSymptoms", "reliefBy","updatedDate", "createdDate")


class SymptomsRecordSerializer(serializers.ModelSerializer):
    """
    Serializer Symptoms Record
    """
    createdDate=serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate=serializers.DateTimeField(default=datetime.datetime.now())
    reportedDate=serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        model = SymptomsRecord
        fields = ('userID', 'symptomsID', 'reportedDate', 'updatedDate',"createdDate")


class SymptomsDefSerializer(serializers.ModelSerializer):
    """
    Serializer Symptoms Definition
    """
    createdDate=serializers.DateTimeField(default=datetime.datetime.now())
    updatedDate=serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        model = SymptomsDef
        fields = ['name', 'description', 'subTitle', 'mediaTitle', "mediaURL", 'describe', 'location',
                  "length", "triggeredBy", "otherSymptoms", "reliefBy", "status", "createdDate" ,"updatedDate"]

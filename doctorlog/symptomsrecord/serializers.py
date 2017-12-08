# coding=utf-8
from rest_framework import serializers
from .models import *


class SymptomsUserSerializer(serializers.ModelSerializer):
    """
    Serializer Symptoms User
    """
    class Meta:
        model = SymptomsUser
        fields = ('userID', 'name', 'subTitle', 'description','describe', 'location', 'length',
                  'triggeredBy', "otherSymptoms", "reliefBy","updatedDate")


class SymptomsRecordSerializer(serializers.ModelSerializer):
    """
    Serializer Symptoms Record
    """
    class Meta:
        model = SymptomsRecord
        fields = ('userID', 'symptomsID', 'reportedDate', 'updatedDate')


class SymptomsDefSerializer(serializers.ModelSerializer):
    """
    Serializer Symptoms Definition
    """
    class Meta:
        model = SymptomsDef
        fields = ['name', 'description', 'subTitle', 'mediaTitle', "mediaURL", 'describe', 'location',
                  "length", "triggeredBy", "otherSymptoms", "reliefBy", "status"]

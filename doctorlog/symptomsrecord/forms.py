from django.forms import ModelForm
from suit.widgets import AutosizedTextarea, SuitSplitDateTimeWidget, EnclosedInput, LinkedSelect
from .models import *


class SymptomsDefForm(ModelForm):
    """
    Symptoms Definition form
    """
    class Meta:
        model = SymptomsDef
        fields = ['name', 'description', 'subTitle', 'mediaTitle', "mediaURL", 'describe', 'location',
                  "length", "triggeredBy", "otherSymptoms", "reliefBy", "status"]
        widgets = {
            "description": AutosizedTextarea,
            "describe": AutosizedTextarea,
            "location": AutosizedTextarea,
            "length": AutosizedTextarea,
            "triggeredBy": AutosizedTextarea,
            "otherSymptoms": AutosizedTextarea,
            "reliefBy": AutosizedTextarea,
            'createdDate': SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget,
            "mediaURL":EnclosedInput(append='icon-globe')
        }


class SymptomRecordForm(ModelForm):
    """
    Symptoms Record form
    """
    class Meta:

        model = SymptomsRecord
        fields = ['userID', 'symptomsID', "reportedDate", 'updatedDate', "status"]
        widgets = {
            'reportedDate': SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget,
            "userID": LinkedSelect,
            "symptomsID": LinkedSelect
        }


class SymptomsUserForm(ModelForm):
    """
    Symptoms User form
    """
    class Meta:

        model = SymptomsUser
        fields = ['userID','name', 'description', 'subTitle', 'mediaTitle', "mediaURL", 'describe', 'location',
                  "length", "triggeredBy", "otherSymptoms", "reliefBy", "status"]
        widgets = {
            "description": AutosizedTextarea,
            "describe": AutosizedTextarea,
            "location": AutosizedTextarea,
            "length": AutosizedTextarea,
            "triggeredBy": AutosizedTextarea,
            "otherSymptoms": AutosizedTextarea,
            "reliefBy": AutosizedTextarea,
            'createdDate': SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget,
            "mediaURL": EnclosedInput(append='icon-globe')
        }

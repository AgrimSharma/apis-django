"""Forms."""
from django.forms import ModelForm
from suit.widgets import SuitSplitDateTimeWidget, EnclosedInput
from .models import VitalReport, Vitals


class VitalsForm(ModelForm):
    """Vitals form."""

    class Meta:
        """Meta."""

        model = Vitals
        fields = ['name', 'description', 'mediaTitle', "mediaURL", "options",
                  "info", "tips", "createdDate", "updatedDate", "status"]
        widgets = {
            "mediaURL": EnclosedInput(append='icon-globe'),
            "createdDate": SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget,

        }


class VitalsRecordForm(ModelForm):
    """Vitals Record form."""

    class Meta:
        """Meta."""

        model = VitalReport
        fields = ['userID', 'vitalID', 'weight', "heartRate", "temperature",
                  "pulse", "sugar", "systol", "dystol", "options", "comment",
                  "createdDate", "updatedDate", "reportedDate", "status"]
        widgets = {
            'weight': EnclosedInput(append="Kg"),
            "heartRate": EnclosedInput(append="bpm"),
            "temperature": EnclosedInput(append="F"),
            "pulse": EnclosedInput(append="bpm",),
            "sugar": EnclosedInput(append="mg/dL"),
            "createdDate": SuitSplitDateTimeWidget,
            "reportedDate": SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget,

        }

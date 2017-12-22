"""# coding=utf-8."""
from django.contrib import admin
from .models import SymptomsDef, SymptomsUser, SymptomsRecord
from .forms import SymptomsDefForm, SymptomRecordForm, SymptomsUserForm


class AdminSymtomsDef(admin.ModelAdmin):
    """Symptoms Definition Admin Panel."""

    form = SymptomsDefForm
    list_display = ('name', 'description')
    fields = [('name', 'description'), 'subTitle', ('mediaTitle', "mediaURL"),
              ('describe', 'location'), ("length", "triggeredBy"),
              ("otherSymptoms", "reliefBy"), "createdDate", "updatedDate",
              "status"]


class AdminSymptomsRecord(admin.ModelAdmin):
    """Symptoms Reports Admin Panel."""

    form = SymptomRecordForm
    list_display = ('userID', 'symptomsID')
    fields = [('userID', 'symptomsID'), "reportedDate", 'updatedDate',
        "status"]


class AdminSymptomsUser(admin.ModelAdmin):
    """Symptoms Definition Admin Panel."""

    form = SymptomsUserForm
    list_display = ('userID', 'name', 'description')
    fields = ["userID", ('name', 'description'), 'subTitle', ('mediaTitle',
        "mediaURL"), ('describe', 'location'), ("length", "triggeredBy"),
    ("otherSymptoms", "reliefBy"), "createdDate", "updatedDate", "status"]


admin.site.register(SymptomsDef, AdminSymtomsDef)
admin.site.register(SymptomsUser, AdminSymptomsUser)
admin.site.register(SymptomsRecord, AdminSymptomsRecord)

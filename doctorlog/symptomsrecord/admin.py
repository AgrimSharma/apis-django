# coding=utf-8
from django.contrib import admin
from .models import *
from .forms import SymptomsDefForm, SymptomRecordForm, SymptomsUserForm


class AdminSymtomsDef(admin.ModelAdmin):
    """
    Symptoms Definition Admin Panel
    """
    form = SymptomsDefForm
    list_display = ('name', 'description')
    fields = [('name', 'description'), 'subTitle', ('mediaTitle', "mediaURL"),
              ('videoTitle', "videoURL"), ('describe', 'location'),
              ("length", "triggeredBy"), ("otherSymptoms", "reliefBy"),
              "createdDate", "updatedDate", "status"]


class AdminSymptomsRecord(admin.ModelAdmin):
    """
    Symptoms Reports Admin Panel
    """

    form = SymptomRecordForm

    list_display = ('user', 'symptom')
    fields = [('userID', 'symptomsID'), "reportedDate", 'updatedDate', "status"]

    def user(self, obj):
        return obj.userID.get_full_name()

    def symptom(self, obj):
        return obj.symptomsID.name


class AdminSymptomsUser(admin.ModelAdmin):
    """
    Symptoms Definition Admin Panel
    """
    form = SymptomsUserForm
    list_display = ('users', 'name', 'description')
    fields = [('name', 'description'), 'subTitle', ('mediaTitle', "mediaURL"),
              ('videoTitle', "videoURL"), ('describe', 'location'),
              ("length", "triggeredBy"), ("otherSymptoms", "reliefBy"),
              "createdDate", "updatedDate", "status"]


    def users(self, obj):
        return obj.userID.get_full_name()

admin.site.register(SymptomsDef, AdminSymtomsDef)
admin.site.register(SymptomsUser, AdminSymptomsUser)
admin.site.register(SymptomsRecord, AdminSymptomsRecord)

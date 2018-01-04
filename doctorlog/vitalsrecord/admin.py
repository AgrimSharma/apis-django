from django.contrib import admin
from .models import *
from .forms import VitalsRecordForm, VitalsForm
# Register your models here.


class AdminVitals(admin.ModelAdmin):
    """
    Vitals Admin Panel
    """
    form = VitalsForm
    list_display = ('name', 'description')
    fields = [('name', 'description'), ('mediaTitle', "mediaURL"), "options", ("info", "tips"),
              "createdDate", "updatedDate", "status"]


class AdminVitalReport(admin.ModelAdmin):
    """
    Vitals Reports Admin Panel
    """
    form = VitalsRecordForm
    list_display = ('user', 'vital')
    fields = [('userID', 'vitalID'), 'weight', "heartRate", 'stressLevel',
              "temperature", "pulse", "sugar", "systol", "dystol", "options", "comment",
              "createdDate", "updatedDate", "reportedDate", "status"]

    def user(self, obj):
        return obj.userID.get_full_name()

    def vital(self, obj):
        return obj.vitalID.name


admin.site.register(Vitals, AdminVitals)
admin.site.register(VitalReport, AdminVitalReport)

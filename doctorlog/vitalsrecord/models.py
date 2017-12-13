from django.db import models
from modules.models import Users
from django.utils.timezone import now


class Vitals(models.Model):
    """
    Vitals model
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    mediaURL = models.URLField(null=True, blank=True)
    mediaTitle = models.CharField(max_length=1000, null=True, blank=True)
    options = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    tips = models.CharField(max_length=1000)
    createdDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + " : " + self.description

    def __unicode__(self):
        return self.name + " : " + self.description


class VitalReport(models.Model):
    """
    Vitals Report model
    """
    userID = models.ForeignKey(Users)
    vitalID = models.ForeignKey(Vitals)
    stressLevel = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    systol = models.CharField(max_length=100)
    dystol = models.CharField(max_length=100)
    heartRate = models.CharField(max_length=10)
    options = models.CharField(max_length=100)
    temperature = models.CharField(max_length=10)
    pulse = models.CharField(max_length=10)
    sugar = models.CharField(max_length=10)
    comment = models.CharField(max_length=1000)
    reportedDate = models.DateTimeField()
    createdDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.userID.firstName + " " + self.userID.lastName + " : " + self.vitalID.name

    def __unicode__(self):
        return self.userID.firstName + " " + self.userID.lastName + " : " + self.vitalID.name

# coding=utf-8
from django.db import models
from modules.models import Users
import django.utils.timezone


class SymptomsDef(models.Model):
    """
    Symptoms Definition model
    """
    name = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    mediaTitle = models.CharField(max_length=1000)
    mediaURL = models.URLField(null=True, blank=True)
    describe = models.TextField()
    location = models.TextField()
    length = models.TextField()
    triggeredBy = models.TextField()
    otherSymptoms = models.TextField()
    reliefBy = models.TextField()
    createdDate = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    updatedDate = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SymptomsUser(models.Model):
    """
    Symptoms Definition model
    """
    userID = models.ForeignKey(Users, related_name="symptom_user")
    name = models.CharField(max_length=100, unique=True)
    subTitle = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    mediaTitle = models.CharField(max_length=1000, null=True, blank=True)
    mediaURL = models.URLField(null=True, blank=True)
    describe = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    length = models.TextField(null=True, blank=True)
    triggeredBy = models.TextField(null=True, blank=True)
    otherSymptoms = models.TextField(null=True, blank=True)
    reliefBy = models.TextField(null=True, blank=True)
    createdDate = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    updatedDate = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.userID.firstName + " " + self.userID.lastName + " : " + self.name

    def __unicode__(self):
        return self.userID.firstName + " " + self.userID.lastName + " : " + self.name


class SymptomsRecord(models.Model):
    """
    Symptoms Definition Record model for Users
    """
    userID = models.ForeignKey(Users, related_name="symptom_report_user")
    symptomsID = models.ForeignKey(SymptomsUser, related_name="symptom_users")
    reportedDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.userID.firstName + " " + self.userID.lastName + " : " + self.symptomsID.name

    def __unicode__(self):
        return self.userID.firstName + " " + self.userID.lastName + " : " + self.symptomsID.name

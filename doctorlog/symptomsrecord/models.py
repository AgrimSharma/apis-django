"""# coding=utf-8."""
from django.db import models
from modules.models import Users


class SymptomsDef(models.Model):
    """Symptoms Definition model."""

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
    createdDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        """meta."""

        ordering = ["name"]

    def __str__(self):
        """str."""
        return self.name

    def __unicode__(self):
        """unicode."""
        return self.name


class SymptomsUser(models.Model):
    """Symptoms Definition model."""

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
    createdDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta."""

        ordering = ["name"]

    def __str__(self):
        """str."""
        return self.userID.first_name + " " + self.userID.last_name
        + " : " + self.name

    def __unicode__(self):
        """unicode."""
        return self.userID.first_name + " " + self.userID.last_name
        + " : " + self.name


class SymptomsRecord(models.Model):
    """Symptoms Definition Record model for Users."""

    userID = models.ForeignKey(Users, related_name="symptom_report_user")
    symptomsID = models.ForeignKey(SymptomsUser, related_name="symptom_users")
    reportedDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        """str."""
        return self.userID.first_name + " " + self.userID.last_name
        + " : " + self.symptomsID.name

    def __unicode__(self):
        """unicode."""
        return self.userID.first_name + " " + self.userID.last_name
        + " : " + self.symptomsID.name

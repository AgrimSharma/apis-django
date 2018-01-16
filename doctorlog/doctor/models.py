from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User
from modules.models import Users
from django.conf import settings
import imghdr
import urllib
from io import StringIO# Used to imitate reading from byte file
from PIL import Image # Holds downloaded image and verifies it
import copy # Copies instances of Image

dose = [('One', 'One'), ("Two", "Two")]
schedule = [('Morning','Morning'), ('AfterNoon', 'AfterNoon'), ('Evening', 'Evening'), ('Night', 'Night')]
medication_type = [('Everyday', 'Everyday'), ('Hourly', 'Hourly'), ('Weekly', 'Weekly')]
remind_me = [('Hourly', 'Hourly'), ('Daily', 'Daily')]


class Doctor(User):
    role = models.CharField(max_length=50, default='Doctor')
    createdDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        """
        get full name of user
        :return: full name
        """
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        """
        over riding save method to save password securely
        :param args:
        :param kwargs:
        :return: None
        """
        self.username = self.email
        super(Doctor, self).save()


class DoctorPatient(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='doctor')
    patient = models.ManyToManyField(Users, related_name='patient')
    createdDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.doctor.email

    def __unicode__(self):
        return self.doctor.email


class DoctorAppointment(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='doctor_appoint')
    patient = models.ForeignKey(Users, related_name='patient_appoint')
    createdDate = models.DateTimeField(null=True, blank=True)
    appointmentDate = models.DateTimeField(null=False, blank=False)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.doctor.get_full_name()

    def __unicode__(self):
        return self.doctor.get_full_name()


class Medication(models.Model):
    """Mediation model."""
    name = models.CharField(max_length=1000)
    dose = models.CharField(choices=dose,max_length=100)
    medicine_pic = models.ImageField(upload_to=settings.MEDIA_ROOT)
    prescribed_by = models.ForeignKey(Doctor)
    schedule = models.CharField(choices=schedule, max_length=100)
    medicine_type = models.CharField(choices=medication_type, max_length=100)
    instructions = models.CharField(max_length=1000)
    remind_me = models.CharField(choices=remind_me, max_length=100)
    refills= models.CharField(max_length=100)
    boxters = models.CharField(max_length=100)
    patient = models.ForeignKey(Users)

    def __str__(self):
        return self.patient.get_full_name() + " - " + self.name

    def __unicode__(self):
        return self.patient.get_full_name() + " - " + self.name

from django.db import models
from django.contrib.auth.models import User
from modules.models import Users


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

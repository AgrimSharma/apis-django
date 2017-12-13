from django.db import models
import django.utils.timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password


roles = (
    ('Doctor', 'Doctor'),
    ('User', 'User'),
)


class Users(models.Model):
    """
    User model for user data insertion
    """
    firstName = models.CharField(max_length=100, error_messages={
            'unique': _("Please provide a first name."),
        })
    lastName = models.CharField(max_length=100, error_messages={
            'unique': _("Please provide a last name."),
        })
    password = models.CharField(_('password'),max_length=20)
    email = models.EmailField(unique=True, error_messages={
            'unique': _("A user with that email already exists."),
        })
    role = models.CharField(max_length=50, choices=roles, default='User')
    createdDate = models.DateTimeField(null=True, blank=True)
    updatedDate = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["firstName"]

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        """
        get full name of user
        :return: full name
        """
        return self.firstName + " " + self.lastName

    def set_password(self, password):
        """
        set password for a user used when we have to change password
        :param password: string
        :return: secure password
        """
        self.password = make_password(password)

    def set_status(self,status):
        """
        set status of a user as True or False
        :param status: Boolean
        :return: None
        """
        self.status = status

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            """
            :param raw_password:
            :return:
            """
            self.set_password(raw_password)
        return check_password(raw_password, self.password, setter)

    def save(self, *args, **kwargs):
        """
        over riding save method to save password securely
        :param args:
        :param kwargs:
        :return: None
        """
        self.password = make_password(self.password)
        super(Users, self).save()

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
    createdDate = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    updatedDate = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["firstName"]

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.firstName + " " + self.lastName

    def set_password(self, password):
        self.password = make_password(password)

    def set_status(self,status):
        self.status = status

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
        return check_password(raw_password, self.password, setter)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Users, self).save()

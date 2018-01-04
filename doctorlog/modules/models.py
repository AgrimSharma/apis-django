from django.contrib.auth.models import User

from django.db import models


class Users(User):
    """
    User model for user data insertion
    """
    role = models.CharField(max_length=50, default='User')
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
        super(Users, self).save()

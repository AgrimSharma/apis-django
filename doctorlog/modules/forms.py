# coding=utf-8
import django.forms
from suit.widgets import AutosizedTextarea, SuitSplitDateTimeWidget, HTML5Input, EnclosedInput
from .models import *


class UserForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = Users
        fields = ['firstName', 'lastName', "email", 'password', 'role', 'status', "createdDate", "updatedDate"]
        widgets = {
            "email": EnclosedInput(append='icon-envelope'),
            "lastName": AutosizedTextarea,
            "firstName": AutosizedTextarea,
            "password": HTML5Input(input_type='password'),
            'createdDate': SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget
        }

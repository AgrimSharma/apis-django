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
        fields = ['first_name', 'last_name', "email", 'password', 'role',
                  'status', "createdDate", "updatedDate"]
        widgets = {
            "first_name": AutosizedTextarea,
            "email": EnclosedInput(append='icon-envelope'),
            "last_name": AutosizedTextarea,
            "password": HTML5Input(input_type='password'),
            'createdDate': SuitSplitDateTimeWidget,
            "updatedDate": SuitSplitDateTimeWidget
        }

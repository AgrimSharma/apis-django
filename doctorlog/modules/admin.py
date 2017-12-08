from django.contrib import admin
from .models import *
from .forms import UserForm
# Register your models here.


class UserAdmn(admin.ModelAdmin):
    """
    User Admin Panel
    """
    form = UserForm
    list_display = ('firstName', 'lastName', 'role')
    fields = [('firstName', 'lastName'), 'password', 'role', "email", 'createdDate', 'updatedDate', 'status']


admin.site.register(Users, UserAdmn)

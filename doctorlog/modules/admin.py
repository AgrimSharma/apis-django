from django.contrib import admin
from .models import *
from .forms import UserForm
# Register your models here.


class UserAdmn(admin.ModelAdmin):
    """
    User Admin Panel
    """
    form = UserForm
    list_display = ('first_name', 'last_name', 'role')
    fields = [('first_name', 'last_name'), 'password', 'role', "email", 'createdDate', 'updatedDate', 'status']


admin.site.register(Users, UserAdmn)

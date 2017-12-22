"""admin."""
from django.contrib import admin
from .models import Users
from .forms import UserForm


class UserAdmn(admin.ModelAdmin):
    """User Admin Panel."""

    form = UserForm
    list_display = ('first_name', 'last_name', 'role')
    fields = [('first_name', 'last_name'), 'password', 'role', "email",
              'createdDate', 'updatedDate', 'status']


admin.site.register(Users, UserAdmn)

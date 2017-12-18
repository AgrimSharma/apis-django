"""
WSGI config for doctorlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

site.addsitedir('/home/pranav/venv/lib/python3.5/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/pranav/apis-django/doctorlog')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doctorlog.settings")

application = get_wsgi_application()

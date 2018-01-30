from django.urls import path, include

from doctorbox_web.api import urls as api_urls
from doctorbox_web.api.admin import admin_site

urlpatterns = [
    path('api/', include(api_urls)),
    path('admin/', admin_site.urls),
]

from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url, include
from rest_framework import routers
from modules import views
from symptomsrecord.views import SymptomsListAPI, SymptomsRecordsAPI, SymptomsRecordsUserAPI, SymptomsListUserAPI, \
    SymptomsDefAPI, SymptomsAPI
from vitalsrecord.views import VitalsReportAPI, VitalsAPI, VitalsReportUserAPI, VitalsNameAPI


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'symptoms', SymptomsListAPI,base_name='test')
router.register(r'symptoms_records', SymptomsRecordsAPI)
router.register(r'vitals', VitalsAPI)
router.register(r'vitals_reports', VitalsReportAPI)
router.register(r'symptoms_def', SymptomsAPI)


urlpatterns = [
    url(r'admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='DoctorBox')),
    url(r'^api/v1/', include(router.urls)),
    url(r'api/v1/ping/$', views.Ping.as_view(), name='ping'),
    url(r'api/v1/symptoms/users/(?P<user_id>[0-9]+)/$', SymptomsListUserAPI.as_view()),
    url(r'api/v1/symptoms/records/users/(?P<user_id>[0-9]+)/$', SymptomsRecordsUserAPI.as_view()),
    url(r'api/v1/symptoms_list/(?P<disease>[\w ]+)/$', views.SymptomsList.as_view()),
    url(r'api/v1/vitals/reports/users/(?P<user_id>[0-9]+)/$', VitalsReportUserAPI.as_view()),
    url(r'api/v1/vitals/by/name/(?P<name>[\w ]+)/$', VitalsNameAPI.as_view()),
    url(r'api/v1/symptoms/def/(?P<name>[a-zA-Z]+)/$', SymptomsDefAPI.as_view()),
    url(r'api/v1/users/email/(?P<email>[\w].+)/$', views.UserByEmailAPI.as_view()),
    url(r'api/v1/users/auth/(?P<email>[\w].+)/(?P<password>[\w].+)/$',
        views.LoginUserAPI.as_view()),
    ]

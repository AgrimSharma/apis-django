from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url, include
from rest_framework import routers
from modules.views import views
from symptomsrecord.views import SymptomsListAPI, SymptomsRecordsAPI, SymptomsRecordsUserAPI, \
    SymptomsListUserAPI, SymptomsDefName, SymptomsAPI
from vitalsrecord.views import VitalsReportAPI, VitalsAPI, VitalsReportUserAPI, VitalsNameAPI
from doctor.views import DoctorViewSet, DoctorPatientViewSet, DoctorAppointmentViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'symptoms', SymptomsListAPI, base_name='test')
router.register(r'symptoms_records', SymptomsRecordsAPI)
router.register(r'vitals', VitalsAPI)
router.register(r'vitals_reports', VitalsReportAPI)
router.register(r'symptoms_def', SymptomsAPI)
router.register(r'doctor', DoctorViewSet)
router.register(r'doctor-patient', DoctorPatientViewSet)
router.register(r'doctor-appointment', DoctorAppointmentViewSet)


urlpatterns = [
    url(r'', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='DoctorBox')),
    url(r'^api/v1/', include(router.urls)),
    url(r'api/v1/ping/$', views.Ping.as_view(), name='ping'),
    url(r'api/v1/vitals/reports/users/', VitalsReportUserAPI.as_view()),
    url(r'api/v1/vitals/by/name/', VitalsNameAPI.as_view()),
    url(r'api/v1/symptoms/by/name/', SymptomsDefName.as_view()),
    url(r'api/v1/authenticate/', views.LoginUserAPI.as_view()),
    url(r'api/v1/users/by/email/', views.UserByEmailAPI.as_view()),
    url(r'api/v1/symptoms/records/users/', SymptomsRecordsUserAPI.as_view()),
    url(r'api/v1/symptoms/by/users/', SymptomsListUserAPI.as_view(),
        name="symptoms_user"),

]

from django.conf.urls import url, include
from rest_framework import routers

from doctorbox_web.api.views import ArticleCategoryViewSet, MedicationViewSet, \
    DoctorViewSet, SymptomViewSet, PrescriptionViewSet, LoggedSymptomViewSet, \
    VitalViewSet

router = routers.DefaultRouter()
router.register(r'medications', MedicationViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'symptoms', SymptomViewSet)
router.register(r'article_categories', ArticleCategoryViewSet)
router.register(r'logged_symptom', LoggedSymptomViewSet)
router.register(r'vitals', VitalViewSet)

urlpatterns = [
    url(r'^1/', include(router.urls)),
    url(r'^1/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

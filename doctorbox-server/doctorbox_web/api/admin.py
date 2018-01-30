from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from doctorbox_web.api.models import Medication, Dosage, Doctor, Article, \
    ArticleCategory, OrderedCategorizedArticle, Symptom, Prescription, \
    Patient, LoggedSymptom, Vital


class DosageArticleInline(admin.TabularInline):
    model = Dosage
    extra = 5


class MedicationAdmin(admin.ModelAdmin):
    inlines = (DosageArticleInline,)


class DoctorAdmin(admin.ModelAdmin):
    pass


class OrderedCategorizedArticleInline(admin.TabularInline):
    model = OrderedCategorizedArticle
    extra = 0


class ArticleCategoryAdmin(admin.ModelAdmin):
    inlines = (OrderedCategorizedArticleInline,)
    ordering = ('order',)


class ArticleAdmin(admin.ModelAdmin):
    pass


class SymptomAdmin(admin.ModelAdmin):
    pass


class PrescriptionAdmin(admin.ModelAdmin):
    pass


class PatientAdmin(admin.ModelAdmin):
    pass


class SymptomDefAdmin(admin.ModelAdmin):
    pass


class LoggedSymptomAdmin(admin.ModelAdmin):
    pass


class VitalAdmin(admin.ModelAdmin):
    pass


class DoctorBoxAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('DoctorBox Admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('DoctorBox administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('DoctorBox administration')


admin_site = DoctorBoxAdminSite()

admin_site.register(Medication, MedicationAdmin)
admin_site.register(Doctor, DoctorAdmin)
admin_site.register(ArticleCategory, ArticleCategoryAdmin)
admin_site.register(Article, ArticleAdmin)
admin_site.register(Symptom, SymptomAdmin)
admin_site.register(Prescription, PrescriptionAdmin)
admin_site.register(Patient, PatientAdmin)
admin_site.register(LoggedSymptom, LoggedSymptomAdmin)
admin_site.register(Vital, VitalAdmin)

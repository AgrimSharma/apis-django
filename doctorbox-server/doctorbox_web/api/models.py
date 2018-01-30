from django.db import models
from django.utils import timezone


class Patient(models.Model):
    identifier = models.AutoField(primary_key=True)
    device_identifier = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.device_identifier)


class Medication(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    friendly_description = models.TextField()
    function = models.CharField(max_length=255)
    video_url = models.URLField(max_length=255)
    information = models.TextField()
    interactions = models.TextField()

    def __str__(self):
        return "{} ({})".format(self.name, self.generic_name)


class Dosage(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    medication = models.ForeignKey(Medication,
                                   related_name='dosages',
                                   on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return "({}) {}".format(self.medication.name, self.name)


class Doctor(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    identifier = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    summary = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=255)
    time_to_read = models.PositiveSmallIntegerField()
    image_url = models.URLField(max_length=255)
    video_url = models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.title


class ArticleCategory(models.Model):
    identifier = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255)
    order = models.PositiveSmallIntegerField()
    articles = models.ManyToManyField(Article, through="OrderedCategorizedArticle")

    class Meta:
        verbose_name_plural = "article categories"

    def __str__(self):
        return self.title


class OrderedCategorizedArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING)
    order = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('article', 'category')

    def __str__(self):
        return "{} - {} ({})".format(self.article.title, self.category.title, self.order)


class Symptom(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    video_title = models.CharField(max_length=255)
    image_title = models.CharField(max_length=255)
    image_url = models.URLField()
    video_url = models.URLField()
    patient_experience = models.TextField()
    location = models.TextField()
    length = models.TextField()
    triggered_by = models.TextField()
    other_symptoms = models.TextField()
    relief_by = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.identifier:
            self.created = now
        self.updated = now
        return super(Symptom, self).save(*args, **kwargs)


class Prescription(models.Model):
    identifier = models.AutoField(primary_key=True)
    medication = models.ForeignKey(to=Medication, on_delete=models.CASCADE)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {} ({})".format(self.medication.name, self.patient.identifier, self.patient.device_identifier)


class LoggedSymptom(models.Model):
    identifier = models.AutoField(primary_key=True)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    patient_experience = models.TextField()
    location = models.TextField()
    length = models.TextField()
    triggered_by = models.TextField()
    other_symptoms = models.TextField()
    relief_by = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["patient"]

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "{}: {} ".format(self.patient.identifier, self.name)

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.identifier:
            self.created = now
        self.updated = now
        return super(LoggedSymptom, self).save(*args, **kwargs)


class Vital(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    media_url = models.URLField(null=True, blank=True)
    media_title = models.CharField(null=True, blank=True, max_length=1000)
    options = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    tips = models.CharField(max_length=1000)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.identifier:
            self.created = now
        self.updated = now
        return super(Vital, self).save(*args, **kwargs)

    def __str__(self):
        return "{} : {}".format(self.name, self.description)

    def __unicode__(self):
        return "{} : {}".format(self.name, self.description)

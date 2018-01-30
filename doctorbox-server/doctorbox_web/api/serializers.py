from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from doctorbox_web.api.models import Medication, Dosage, Doctor, \
    ArticleCategory, Article, OrderedCategorizedArticle, Symptom, \
    Prescription, LoggedSymptom, Vital


class MedicationSerializer(serializers.HyperlinkedModelSerializer):
    dosages = serializers.HyperlinkedIdentityField(view_name="medication-dosages")

    class Meta:
        model = Medication
        fields = ('identifier', 'name', 'generic_name', 'function', 'friendly_description', 'video_url', 'dosages',
                  'information', 'interactions')


class DosageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dosage
        fields = ('name',)


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name',)


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('identifier', 'title', 'summary', 'body', 'author', 'time_to_read', 'image_url', 'video_url')


class ArticleCategorySerializer(serializers.HyperlinkedModelSerializer):
    articles = SerializerMethodField()

    def get_articles(self, obj):
        query_set = OrderedCategorizedArticle.objects.filter(category__pk=obj.pk)
        query_set = query_set.order_by('order').prefetch_related('article')
        article_list = [oca.article for oca in query_set]
        article_serializer = ArticleSerializer(article_list, many=True, read_only=True)

        return article_serializer.data

    class Meta:
        model = ArticleCategory
        fields = ('identifier', 'title', 'articles', 'image_url')


class SymptomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symptom
        fields = ('identifier', 'name', 'image_url', 'subtitle', 'image_title', 'location', 'length', 'description',
                  'triggered_by', 'other_symptoms', 'relief_by', 'status', 'created', 'updated')


class ReadPrescriptionSerializer(serializers.HyperlinkedModelSerializer):
    medication = MedicationSerializer()

    class Meta:
        model = Prescription
        fields = ('identifier', 'medication')


class WritePrescriptionSerializer(serializers.ModelSerializer):
    medication = serializers.IntegerField()

    def create(self, validated_data):
        patient = self.context['request'].patient
        prescription = Prescription(patient=patient, medication_id=validated_data['medication'])
        prescription.save()

        return prescription

    class Meta:
        model = Prescription
        fields = ('medication',)


class LoggedSymptomSerializer(serializers.ModelSerializer):
    """Serializer Logged Symptoms."""

    class Meta:
        model = LoggedSymptom
        fields = ['patient', 'name', 'patient_experience', 'location',
                  'length', 'triggeredBy', 'otherSymptoms',
                  'reliefBy', 'status']


class VitalSerializer(serializers.ModelSerializer):
    """
    Vital Serializer to serialize data from models
    """

    class Meta:
        model = Vital
        fields = ('name', 'description', 'media_title', 'media_url', 'options',
                  'info', 'tips', 'updated', 'created')

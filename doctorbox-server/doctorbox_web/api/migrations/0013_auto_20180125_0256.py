# Generated by Django 2.0 on 2018-01-25 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20180120_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedSymptom',
            fields=[
                ('identifier', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('patient_experience', models.TextField()),
                ('location', models.TextField()),
                ('length', models.TextField()),
                ('triggered_by', models.TextField()),
                ('other_symptoms', models.TextField()),
                ('relief_by', models.TextField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Patient')),
            ],
            options={
                'ordering': ['patient'],
            },
        ),
        migrations.AddField(
            model_name='symptom',
            name='patient_experience',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='symptom',
            name='video_title',
            field=models.CharField(default='Video title goes here', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='symptom',
            name='video_url',
            field=models.URLField(default='https://example.com/video_url'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='symptom',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='image_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='length',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='location',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]

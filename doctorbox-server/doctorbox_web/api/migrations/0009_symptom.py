# Generated by Django 2.0 on 2018-01-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180112_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('identifier', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField(max_length=255)),
            ],
        ),
    ]

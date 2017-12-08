# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules', '0003_auto_20171206_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='VitalReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=10)),
                ('systol', models.CharField(max_length=100)),
                ('dystol', models.CharField(max_length=100)),
                ('heartRate', models.CharField(max_length=10)),
                ('options', models.CharField(max_length=100)),
                ('temperature', models.CharField(max_length=10)),
                ('pulse', models.CharField(max_length=10)),
                ('sugar', models.CharField(max_length=10)),
                ('comment', models.CharField(max_length=1000)),
                ('reportedDate', models.DateTimeField()),
                ('createdDate', models.DateTimeField(blank=True, null=True)),
                ('updatedDate', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vital_record', to='modules.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('mediaURL', models.URLField(blank=True, null=True)),
                ('mediaTitle', models.CharField(blank=True, max_length=1000, null=True)),
                ('options', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=100)),
                ('tips', models.CharField(max_length=1000)),
                ('createdDate', models.DateTimeField(blank=True, null=True)),
                ('updatedDate', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vital_user', to='modules.Users')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='vitalreport',
            name='vitalID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitalsrecord.Vitals'),
        ),
    ]

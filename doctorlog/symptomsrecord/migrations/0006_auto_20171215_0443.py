# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-15 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptomsrecord', '0005_auto_20171208_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptomsdef',
            name='createdDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='describe',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='length',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='mediaTitle',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='otherSymptoms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='reliefBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='triggeredBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='updatedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsrecord',
            name='updatedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsuser',
            name='createdDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symptomsuser',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='symptomsuser',
            name='updatedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

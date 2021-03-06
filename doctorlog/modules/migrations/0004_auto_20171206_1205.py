# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-06 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_auto_20171206_0706'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SymptomsDef',
        ),
        migrations.RemoveField(
            model_name='symptomsrecord',
            name='symptomsID',
        ),
        migrations.RemoveField(
            model_name='symptomsrecord',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='symptomsuser',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='vitalreport',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='vitalreport',
            name='vitalID',
        ),
        migrations.DeleteModel(
            name='SymptomsRecord',
        ),
        migrations.DeleteModel(
            name='SymptomsUser',
        ),
        migrations.DeleteModel(
            name='VitalReport',
        ),
        migrations.DeleteModel(
            name='Vitals',
        ),
    ]

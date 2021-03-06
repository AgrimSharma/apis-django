# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-08 08:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vitalsrecord', '0005_auto_20171208_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalreport',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 8, 0, 17, 711114, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='vitalreport',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 8, 0, 17, 711159, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 8, 0, 17, 709793, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 8, 0, 17, 709840, tzinfo=utc), null=True),
        ),
    ]

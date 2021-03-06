# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-08 06:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symptomsrecord', '0002_auto_20171208_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptomsdef',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 6, 6, 50, 85669, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='symptomsdef',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 6, 6, 50, 85719, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='symptomsrecord',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 6, 6, 50, 88253, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='symptomsuser',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 6, 6, 50, 86984, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='symptomsuser',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 6, 6, 50, 87029, tzinfo=utc), null=True),
        ),
    ]

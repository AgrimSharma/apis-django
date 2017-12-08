# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-08 06:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_auto_20171207_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 6, 5, 53, 254560, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='updatedDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 6, 5, 53, 254618, tzinfo=utc), null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-16 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_auto_20180116_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='medicine_pic',
            field=models.ImageField(upload_to='/home/pranav/apis-django/doctorlog/media'),
        ),
    ]
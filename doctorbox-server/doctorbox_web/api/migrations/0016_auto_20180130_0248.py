# Generated by Django 2.0 on 2018-01-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_vitals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitals',
            name='media_title',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

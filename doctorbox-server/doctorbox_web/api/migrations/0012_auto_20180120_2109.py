# Generated by Django 2.0 on 2018-01-20 21:09

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('api', '0011_patientdevice_prescription'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PatientDevice',
            new_name='Patient',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='patient_device',
            new_name='patient',
        ),
    ]
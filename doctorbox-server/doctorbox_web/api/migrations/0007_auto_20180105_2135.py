# Generated by Django 2.0 on 2018-01-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
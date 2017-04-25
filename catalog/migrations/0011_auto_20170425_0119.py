# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 01:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20170419_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donation_list',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='event_date_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='date_entered',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'Date entered into this database'),
        ),
    ]

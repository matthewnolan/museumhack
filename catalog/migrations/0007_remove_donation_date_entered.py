# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 04:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_donation_date_entered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='date_entered',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 20:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20170407_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='ammount',
            new_name='amount',
        ),
    ]

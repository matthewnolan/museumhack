# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 05:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='company',
        ),
        migrations.RemoveField(
            model_name='person',
            name='linkedin',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170407_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='donorgroup',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='person',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.DeleteModel(
            name='Donorgroup',
        ),
        migrations.DeleteModel(
            name='Institution',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]

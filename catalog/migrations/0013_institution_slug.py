# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20170517_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='slug',
            field=models.SlugField(default=None, null=True, unique=True),
        ),
    ]
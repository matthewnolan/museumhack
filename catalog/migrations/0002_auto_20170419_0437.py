# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount_exact',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'For exact values ie: $100', max_digits=99, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='amount_range_high',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'For high end $100-$200', max_digits=99, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='amount_range_low',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'For range low end ie: $100-$200 or for low end of range ie: $100 and above', max_digits=99, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_type',
            field=models.CharField(choices=[(b'e', b'Exact Value: $100'), (b'r', b'Range: $100-$200'), (b'p', b'Range: $100 and above'), (b'o', b'Just other'), (b'u', b'Unknown')], default=b'u', help_text=b'Donation Type', max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
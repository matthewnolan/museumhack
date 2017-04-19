# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text=b'Unique ID for this particular donation', primary_key=True, serialize=False)),
                ('donation_full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('donation_class', models.CharField(blank=True, max_length=500, null=True)),
                ('event_name', models.CharField(blank=True, max_length=500, null=True)),
                ('donation_type', models.CharField(choices=[(b'e', b'Exact Value: $100'), (b'r', b'Range: $100-$200'), (b'p', b'Range: $100 and above'), (b'o', b'Just other'), (b'u', b'Unknown')], default=b'e', help_text=b'Donation Type', max_length=1)),
                ('amount_exact', models.DecimalField(decimal_places=2, default=0, help_text=b'For exact values ie: $100', max_digits=99)),
                ('amount_range_low', models.DecimalField(decimal_places=2, default=0, help_text=b'For range low end ie: $100-$200 or for low end of range ie: $100 and above', max_digits=99)),
                ('amount_range_high', models.DecimalField(decimal_places=2, default=0, help_text=b'For high end $100-$200', max_digits=99)),
                ('amount_other', models.CharField(blank=True, help_text=b'ie: Plus a special gift from our family', max_length=500, null=True)),
                ('donation_date_start', models.DateField(blank=True, null=True)),
                ('donation_date_end', models.DateField(blank=True, null=True)),
                ('collection_date', models.DateField(blank=True, null=True)),
                ('data_source_name', models.CharField(blank=True, max_length=500, null=True)),
                ('data_source_url', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donorgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'Name of the group of donors', max_length=200)),
                ('year', models.IntegerField(default=b'2013', help_text=b'Year of this group')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'John Doe', max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='donorgroup',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Institution'),
        ),
        migrations.AddField(
            model_name='donation',
            name='donorgroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Donorgroup'),
        ),
        migrations.AddField(
            model_name='donation',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Institution'),
        ),
        migrations.AddField(
            model_name='donation',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Person'),
        ),
    ]

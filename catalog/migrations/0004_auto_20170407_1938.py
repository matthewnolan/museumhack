# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170407_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular donation', primary_key=True, serialize=False)),
                ('ammount', models.CharField(max_length=500)),
                ('donation_date', models.DateField(blank=True, null=True)),
                ('collection_date', models.DateField(blank=True, null=True)),
                ('data_source_name', models.CharField(max_length=500)),
                ('data_source_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Donorgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the group of donors', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('linkedin', models.URLField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='died'),
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
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0010_auto_20171113_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateexam',
            name='time_period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database_management.TimeExam'),
        ),
    ]

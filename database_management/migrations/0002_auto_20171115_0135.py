# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='schedule_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database_management.ScheduleRoom'),
        ),
        migrations.AddField(
            model_name='scheduleroom',
            name='proj_id',
            field=models.IntegerField(default=0),
        ),
    ]

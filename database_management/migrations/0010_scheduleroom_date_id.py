# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 09:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0009_auto_20180123_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleroom',
            name='date_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database_management.DateExam'),
        ),
    ]
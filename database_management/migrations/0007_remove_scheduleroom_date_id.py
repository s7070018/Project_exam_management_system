# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0006_remove_teacher_proj_group_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleroom',
            name='date_id',
        ),
    ]

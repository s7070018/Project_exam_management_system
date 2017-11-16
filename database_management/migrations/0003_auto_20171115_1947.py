# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0002_auto_20171115_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='schedule_teacher',
            field=models.ManyToManyField(to='database_management.ScheduleRoom'),
        ),
        migrations.AlterField(
            model_name='project',
            name='schedule_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database_management.ScheduleRoom'),
        ),
    ]

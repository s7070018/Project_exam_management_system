# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-20 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0018_auto_20180321_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='levels_teacher',
            field=models.FloatField(default=0),
        ),
    ]

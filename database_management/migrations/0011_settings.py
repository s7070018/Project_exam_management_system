# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0010_scheduleroom_date_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load', models.IntegerField(default=0)),
                ('activate', models.BooleanField(default=True)),
                ('forms', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'ตาราง คะแนนที่ปรึกษา',
            },
        ),
    ]

# Generated by Django 2.0.3 on 2018-04-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0025_auto_20180411_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='proj_group_exam',
            field=models.IntegerField(default=0),
        ),
    ]
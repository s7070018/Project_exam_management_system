# Generated by Django 2.0.3 on 2018-04-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0024_auto_20180411_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=1024),
        ),
    ]

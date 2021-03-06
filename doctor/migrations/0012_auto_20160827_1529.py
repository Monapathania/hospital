# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-27 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_auto_20160827_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdevicesforpatient',
            name='PulseMonitor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registerdevicesforpatient',
            name='SugarMonitoringDevice',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registerdevicesforpatient',
            name='TemperatureMonitor',
            field=models.BooleanField(default=False),
        ),
    ]

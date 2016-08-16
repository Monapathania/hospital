# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-04 07:33
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_employee_group'),
        ('appointments', '0004_auto_20160310_0812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='DateOfBirth',
            new_name='DateOfAppointment',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='NameOfDoctor',
        ),
        migrations.AddField(
            model_name='appointment',
            name='EmployeeID',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='Remarks',
            field=models.TextField(default=datetime.datetime(2016, 8, 4, 7, 33, 24, 438000, tzinfo=utc), max_length='300', verbose_name='Remarks or Comments'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='PatientId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

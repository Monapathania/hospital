# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-04 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20160804_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='City',
            field=models.CharField(default='Chandigarh', max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Employee_Name',
            field=models.CharField(default='Mona', max_length=254),
        ),
    ]

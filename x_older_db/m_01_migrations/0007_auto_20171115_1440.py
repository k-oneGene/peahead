# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selfdata', '0006_auto_20171115_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pomodoro',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='weight',
            options={'managed': True},
        ),
    ]
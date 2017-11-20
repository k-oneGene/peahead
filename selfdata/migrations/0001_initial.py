# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoogleFit',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, db_column='Date', null=True)),
                ('calories_kcal_field', models.FloatField(blank=True, db_column='Calories (kcal)', null=True)),
                ('step_count', models.IntegerField(blank=True, db_column='Step count', null=True)),
                ('cycling_duration_ms_field', models.IntegerField(blank=True, db_column='Cycling duration (ms)', null=True)),
                ('inactive_duration_ms_field', models.IntegerField(blank=True, db_column='Inactive duration (ms)', null=True)),
                ('walking_duration_ms_field', models.IntegerField(blank=True, db_column='Walking duration (ms)', null=True)),
                ('running_duration_ms_field', models.IntegerField(blank=True, db_column='Running duration (ms)', null=True)),
            ],
            options={
                'db_table': 'google_fit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, db_column='Date', null=True)),
                ('mood', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mood',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nootropic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, db_column='Date', null=True)),
                ('nootropic', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nootropic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pomodoro',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, db_column='Date', null=True)),
                ('record_date', models.TextField(blank=True, db_column='record_date', null=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('subject_none', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pomodoro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PomoExcelDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, db_column='Date', null=True)),
                ('pomo_total', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pomo_excel_daily',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PomoKanbanDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, db_column='Date', null=True)),
                ('pomo_total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pomo_kanban_daily',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, db_column='date', null=True)),
                ('total_hours', models.FloatField(blank=True, null=True)),
                ('sleep_time', models.TextField(blank=True, db_column='sleep_time', null=True)),
            ],
            options={
                'db_table': 'sleep',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeatherDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, db_column='Date', null=True)),
                ('temp_mean', models.FloatField(blank=True, db_column='Temp_mean', null=True)),
                ('temp_min', models.FloatField(blank=True, db_column='Temp_min', null=True)),
                ('temp_max', models.FloatField(blank=True, db_column='Temp_max', null=True)),
                ('humid_mean', models.FloatField(blank=True, db_column='Humid_mean', null=True)),
                ('sun_total', models.FloatField(blank=True, db_column='Sun_total', null=True)),
                ('rain_total', models.FloatField(blank=True, db_column='Rain_total', null=True)),
            ],
            options={
                'db_table': 'weather_daily',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, db_column='Date', null=True)),
                ('weight', models.FloatField(blank=True, db_column='Weight', null=True)),
                ('bmi', models.FloatField(blank=True, db_column='BMI', null=True)),
                ('fat', models.FloatField(blank=True, db_column='Fat', null=True)),
            ],
            options={
                'db_table': 'weight',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=120)),
            ],
        ),
    ]

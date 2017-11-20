# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class GoogleFit(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    calories_kcal_field = models.FloatField(db_column='Calories (kcal)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    step_count = models.IntegerField(db_column='Step count', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cycling_duration_ms_field = models.IntegerField(db_column='Cycling duration (ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    inactive_duration_ms_field = models.IntegerField(db_column='Inactive duration (ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    walking_duration_ms_field = models.IntegerField(db_column='Walking duration (ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    running_duration_ms_field = models.IntegerField(db_column='Running duration (ms)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'google_fit'


class Mood(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mood = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mood'


class Nootropic(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nootropic = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nootropic'


class PomoExcelDaily(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pomo_total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pomo_excel_daily'


class PomoKanbanDaily(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pomo_total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pomo_kanban_daily'


class Pomodoro(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    subject = models.TextField(blank=True, null=True)
    subject_none = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pomodoro'


class Sleep(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_hours = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sleep'


class WeatherDaily(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_mean = models.FloatField(db_column='Temp_mean', blank=True, null=True)  # Field name made lowercase.
    temp_min = models.FloatField(db_column='Temp_min', blank=True, null=True)  # Field name made lowercase.
    temp_max = models.FloatField(db_column='Temp_max', blank=True, null=True)  # Field name made lowercase.
    humid_mean = models.FloatField(db_column='Humid_mean', blank=True, null=True)  # Field name made lowercase.
    sun_total = models.FloatField(db_column='Sun_total', blank=True, null=True)  # Field name made lowercase.
    rain_total = models.FloatField(db_column='Rain_total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weather_daily'


class Weight(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
    fat = models.FloatField(db_column='Fat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weight'


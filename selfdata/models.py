# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# For now to get it working instead of using today's or yesterday's date
def default_date():
    now = datetime.now()
    now_fixed = datetime(now.year, now.month, now.day)
    return now_fixed

def default_week():
    now = datetime.now()
    if now.isocalendar()[1] < 10:
        q_week = str(now.isocalendar()[0]) + '-W0' + str(now.isocalendar()[1])
    else:
        q_week = str(now.isocalendar()[0]) + '-W' + str(now.isocalendar()[1])

    return q_week

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class GoogleFit(models.Model):
    index = models.IntegerField(primary_key=True)
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

    def get_steps(self, q_date):
        if q_date == None:
            # q_date = datetime.strptime('2017-09-30 00:00:00', '%Y-%m-%d %H:%M:%S')
            #todo: use today's date
            # q_date = datetime.strptime('2017-09-30', '%Y-%m-%d')
            # q_date = datetime.now().date()
            q_date = default_date()
        query = self.objects.filter(date__contains=q_date)
        steps_value = None
        if query.exists():
            steps_value = query.get().step_count
        else:
            steps_value = 'x'

        return steps_value

    def get_week(self, q_week, q_week_end=None):
        if q_week is None:
            q_week = default_week()
        if q_week_end is None:
            q_week_end = q_week

        qry_avg_set = self.objects.raw(f'''
        SELECT "index" as "index", weekNumber, Round(Avg(avg_1_steps), 1) as avg_steps
        FROM (
            SELECT "index" as "index", date(Date) AS just_date, STRFTIME('%%Y-W%%W', date(DATE)) AS weekNumber, Avg("Step count") AS avg_1_steps
            FROM google_fit
            WHERE weekNumber BETWEEN "{q_week}" AND "{q_week_end}"
            GROUP BY weekNumber
            )
            ''')

        try:
            if qry_avg_set[0].avg_steps is not None:
                average_value = qry_avg_set[0].avg_steps
            else:
                average_value = 'x'
        except:
            average_value = 'x'
        return average_value


class Mood(models.Model):
    index = models.IntegerField(primary_key=True)#blank=True, null=True
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mood = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False #Used
        db_table = 'mood'

    def __str__(self):
        return datetime.strftime(self.date, format='%Y-%m-%d')
    
    def get_mood(self, q_date):
        if q_date == None:
            q_date = default_date()
        mood = self.objects.filter(date__contains=q_date)
        mood_value = None
        if mood.exists():
            mood_value = mood.get().mood
        else:
            mood_value = 'x'
        return mood_value

    def get_week(self, q_week, q_week_end=None):
        if q_week is None:
            q_week = default_week()
        if q_week_end is None:
            q_week_end = q_week

        #TODO: Try to get it working ORM way at some point.
        '''
        # select_data = {'weekNumber': """STRFTIME('%Y-W%W', date(Date))"""}
        # mood = self.objects.extra(select=select_data).values('weekNumber').annotate(Avg("mood"))

        # mood = self.objects.annotate(weekNumber=RawSQL("""
        # SELECT STRFTIME('%%Y-W%%W', date(Date)) AS weekNumber
        # WHERE weekNumber BETWEEN %s AND  %s""", ("2017-W15", "2017-W19",)))

        # mood = self.objects.annotate(weekNumber=RawSQL("""
        # SELECT STRFTIME('%%Y-W%%W', date(Date)) AS weekNumber
        # WHERE weekNumber = %s""", ("2017-W15",)))

        # mood = mood.count()

        # mood_value = mood
        # print(mood_value)
        '''

        qry_avg_set = self.objects.raw(f'''
        SELECT "index" as "index", weekNumber, Round(Avg(avg_1_mood), 1) as avg_mood
        FROM (
            SELECT "index" as "index", date(Date) AS just_date, STRFTIME('%%Y-W%%W', date(DATE)) AS weekNumber, Avg(mood) AS avg_1_mood
            FROM mood
            WHERE weekNumber BETWEEN "{q_week}" AND "{q_week_end}"
            GROUP BY weekNumber
            )
        LIMIT 1
            ''')

        try:
            if qry_avg_set[0].avg_mood is not None:
                average_value = qry_avg_set[0].avg_mood
            else:
                average_value = 'x'
        except:
            average_value = 'x'
        return average_value



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
    index = models.IntegerField(primary_key=True) #blank=True, null=True
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    record_date = models.TextField(db_column='record_date', blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    subject_none = models.TextField(blank=True, null=True)

    class Meta:
        managed = False #Used
        db_table = 'pomodoro'

    def get_pomo(self, q_date):
        if q_date == None:
            q_date = default_date()
            q_date = q_date.strftime("%Y-%m-%d")
        pomodoro = self.objects.raw(f'''
            SELECT "index" as "index", Date, date(record_date) AS just_date,record_date, ROUND(count(record_date),1) AS total_pomo
            FROM pomodoro
            WHERE subject IS NOT NULL and just_date IS "{q_date}"
            GROUP BY just_date
            LIMIT 1''')
        if len(list(pomodoro)) != 0:
            pomodoro_total_value = pomodoro[0].total_pomo
        else:
            pomodoro_total_value = 'x'
        return pomodoro_total_value

    def get_week_total(self, q_week, q_week_end=None):
        if q_week is None:
            q_week = default_week()
        if q_week_end is None:
            q_week_end = q_week

        qry_avg_set = self.objects.raw(f'''
            SELECT "index" as "index", SUM(total_1_pomo) AS total_pomo
            FROM (
                SELECT "index" as "index", date(record_date) AS just_date, STRFTIME('%%Y-W%%W', date(record_date)) AS weekNumber, Count(record_date) AS total_1_pomo
                FROM pomodoro
                WHERE 
                    subject IS NOT NULL AND
                    weekNumber BETWEEN "{q_week}" AND "{q_week_end}"
                GROUP BY weekNumber
                )
            ''')

        try:
            if qry_avg_set[0].total_pomo is not None:
                average_value = qry_avg_set[0].total_pomo
            else:
                average_value = 'x'
        except:
            average_value = 'x'
        return average_value

    def get_week_avg(self, q_week, q_week_end=None):
        if q_week is None:
            q_week = default_week()
        if q_week_end is None:
            q_week_end = q_week

        qry_avg_set = self.objects.raw(f'''
        SELECT "index" as "index", weekNumber, ROUND(Avg(pomo_per_working_day), 1) as avg_pomo
        FROM (
            SELECT "index" as "index", date(record_date) AS just_date, STRFTIME('%%Y-W%%W', date(record_date)) AS weekNumber, Count(record_date) AS total_pomo, Count(record_date)/5 AS pomo_per_working_day
            FROM pomodoro
            WHERE 
                subject IS NOT NULL AND
                weekNumber BETWEEN "{q_week}" AND "{q_week_end}"
            GROUP BY weekNumber
            )
            ''')

        try:
            if qry_avg_set[0].avg_pomo is not None:
                average_value = qry_avg_set[0].avg_pomo
            else:
                average_value = 'x'
        except:
            average_value = 'x'
        return average_value


class Sleep(models.Model):
    index = models.IntegerField(primary_key=True)
    date = models.TextField(db_column='date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_hours = models.FloatField(blank=True, null=True)
    sleep_time = models.TextField(db_column='sleep_time', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sleep'

    def get_sleep_total_hours(self, q_date):
        if q_date == None:
            q_date = default_date()
        sleep = self.objects.filter(date__contains=q_date)
        if sleep.exists():
            sleep_value = sleep.get().total_hours
        else:
            sleep_value = 'x'
        return sleep_value

    def get_sleep_time(self, q_date):
        if q_date == None:
            q_date = default_date()
        sleep = self.objects.filter(date__contains=q_date)
        print(q_date)

        if sleep.exists():
            sleep_value = sleep.get().sleep_time.time()
            print(type(sleep_value))
        else:
            sleep_value = 'x'
        return sleep_value

    def get_week_sleep_total_hours(self, q_week, q_week_end=None):
        if q_week is None:
            q_week = default_week()
        if q_week_end is None:
            q_week_end = q_week

        qry_avg_set = self.objects.raw(f'''
        SELECT "index" as "index", weekNumber, Round(Avg(avg_1_sleep), 1) as avg_sleep
        FROM (
            SELECT "index" as "index", date(Date) AS just_date, STRFTIME('%%Y-W%%W', date(DATE)) AS weekNumber, Avg("total_hours") AS avg_1_sleep
            FROM sleep
            WHERE weekNumber BETWEEN "{q_week}" AND "{q_week_end}"
            GROUP BY weekNumber
            )
        LIMIT 1
            ''')

        try:
            if qry_avg_set[0].avg_sleep is not None:
                average_value = qry_avg_set[0].avg_sleep
            else:
                average_value = 'x'
        except:
            average_value = 'x'
        return average_value

    def get_week_sleep_total_hours_avg(self, q_week, q_week_end=None):
        if q_week is None:
            q_week = default_week()
        if q_week_end is None:
            q_week_end = q_week

        qry_avg_set = self.objects.raw(f'''
        SELECT "index" as "index", weekNumber, Round(Avg(avg_1_sleep), 1) as avg_sleep
        FROM (
            SELECT "index" as "index", date(Date) AS just_date, STRFTIME('%%Y-W%%W', date(DATE)) AS weekNumber, Avg("total_hours") AS avg_1_sleep
            FROM sleep
            WHERE weekNumber BETWEEN "{q_week}" AND "{q_week_end}"
            GROUP BY weekNumber
            )
        LIMIT 1
            ''')

        try:
            if qry_avg_set[0].avg_sleep is not None:
                average_value = qry_avg_set[0].avg_sleep
            else:
                average_value = 'x'
        except:
            average_value = 'x'
        average_value = 'need to have raw sleep data'
        return average_value


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
    index = models.IntegerField(primary_key=True) # blank=True, null=True
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
    fat = models.FloatField(db_column='Fat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False #Used
        db_table = 'weight'

    def get_weight(self, q_date):
        if q_date == None:
            q_date = default_date()
        weight = self.objects.filter(date__contains=q_date)

        if weight.exists():
            weight_value = weight.get().weight
        else:
            weight_value = 'x'
        return weight_value

    def get_week(self, q_week, q_week_end=None):
        if q_week is None:
            q_week = default_week()
        if q_week_end is None:
            q_week_end = q_week

        qry_avg_set = self.objects.raw(f'''
        SELECT "index" as "index", weekNumber, Round(Avg(avg_1_weight), 1) as avg_weight
        FROM (
            SELECT "index" as "index", date(Date) AS just_date, STRFTIME('%%Y-W%%W', date(DATE)) AS weekNumber, Avg("Weight") AS avg_1_weight
            FROM weight
            WHERE weekNumber BETWEEN "{q_week}" AND "{q_week_end}"
            GROUP BY weekNumber
            )
        LIMIT 1
            ''')

        try:
            if qry_avg_set[0].avg_weight is not None:
                average_value = qry_avg_set[0].avg_weight
            else:
                average_value = 'x'
        except:
            average_value = 'x'
        return average_value


class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=120)


class Test2(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=120)
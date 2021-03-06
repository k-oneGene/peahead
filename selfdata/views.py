from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.urls import reverse
from django.http import JsonResponse
import json

from .models import Mood, Pomodoro, Weight, GoogleFit, Sleep

from selfdata.Report.report_multiples import graph_report, graph_report_one, graph_get_x_y

from .utils import month_to_week
from .Report.util_report_config import tbl_name_web_temp_rev

import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.

# def home(request):
#     html = "<h1>Hello world</h1>"
#     return HttpResponse(html)


class Selfdata_main(TemplateView):
    template_name = "selfdata_main.html"
    # def get(self, request, *args, **kwargs):
    #     return render(request, )


class Selfdata_detail(TemplateView):
    template_name = "selfdata_detail.html"

    def get_context_data(self, **kwargs):
        context = super(Selfdata_detail, self).get_context_data(**kwargs)
        q_start = self.request.GET.get('q_start')
        q_end = self.request.GET.get('q_end')

        print(q_start)
        print(q_end)

        if q_start is None:
            print("'it's true'")
            q_start = '2017-03-01'
            q_end = '2017-04-20'

        # print(q_start)
        # print(q_end)
        # print(kwargs['slug'])
        context['sd_type'] = kwargs['slug'] + '.svg'
        if q_start and q_end:
            tbl_name = tbl_name_web_temp_rev[kwargs['slug']]
            x_axis, y_axis= graph_get_x_y(q_start, q_end, tbl_name)
            # context['axises'] = dict(zip(x_axis, y_axis))

            context['g_x_label'] = kwargs['slug'].capitalize()
            context['x_axis'] = [new_x_axis[0:10] for new_x_axis in x_axis]
            context['y_axis'] = y_axis

            context['q_start'] = q_start
            context['q_end'] = q_end

        return context


class Selfdata_dashboard(TemplateView):
    template_name = "selfdata_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Selfdata_dashboard, self).get_context_data(**kwargs)
        context['q_date'] = self.request.GET.get('q_date')

        if context['q_date'] is None:
            context['q_date'] = '2017-07-12'

        context['slept_time'] = Sleep.get_sleep_time(Sleep, context['q_date'])
        context['sleep'] = Sleep.get_sleep_total_hours(Sleep, context['q_date'])
        context['pomodoro'] = Pomodoro.get_pomo(Pomodoro, context['q_date'])
        context['weight'] = Weight.get_weight(Weight, context['q_date'])
        context['steps'] = GoogleFit.get_steps(GoogleFit, context['q_date'])
        context['mood'] = Mood.get_mood(Mood, context['q_date'])

        # This also works.
        # context['q_date'] = self.request.GET['q_date']
        return context


class Selfdata_dashboard_week(TemplateView):
    template_name = "selfdata_dashboard_week.html"

    def get_context_data(self, **kwargs):
        context = super(Selfdata_dashboard_week, self).get_context_data(**kwargs)
        context['q_week'] = self.request.GET.get('q_week')

        if context['q_week'] is None:
            context['q_week'] = '2017-W31'

        context['slept_time'] = Sleep.get_week_sleep_total_hours_avg(Sleep, context['q_week'])
        context['sleep'] = Sleep.get_week_sleep_total_hours(Sleep, context['q_week'])
        context['pomodoro_total'] = Pomodoro.get_week_total(Pomodoro, context['q_week'])
        context['pomodoro_per'] = Pomodoro.get_week_avg(Pomodoro, context['q_week'])
        context['weight'] = Weight.get_week(Weight, context['q_week'])
        context['steps'] = GoogleFit.get_week(GoogleFit, context['q_week'])
        context['mood'] = Mood.get_week(Mood, context['q_week'])
        context['week_num_now'] = datetime.datetime.now().isocalendar()[1]

        # TODO: Need validation and cleaning for people typing in random data

        if context['q_week'] is not None:
            week = context['q_week'].split('-W')
            context['week'] = f'{week[0]} - Week {week[1]}'
        else:
            context['week'] = ''

        return context


class Selfdata_dashboard_week_2(TemplateView):
    template_name = "selfdata_dashboard_week_2.html"

    def get_context_data(self, **kwargs):
        context = super(Selfdata_dashboard_week_2, self).get_context_data(**kwargs)
        context['q_week'] = self.request.GET.get('q_week')
        context['q_week_end'] = self.request.GET.get('q_week_end')

        print(context['q_week'])
        print(context['q_week_end'])

        if context['q_week'] is None:
            if context['q_week_end'] is None:
                context['q_week'] = '2017-W42'
                context['q_week_end'] = '2017-W47'



        context['slept_time'] = Sleep.get_week_sleep_total_hours_avg(Sleep, context['q_week'], context['q_week_end'])
        context['sleep'] = Sleep.get_week_sleep_total_hours(Sleep, context['q_week'], context['q_week_end'])
        context['pomodoro_total'] = Pomodoro.get_week_total(Pomodoro, context['q_week'], context['q_week_end'])
        context['pomodoro_per'] = Pomodoro.get_week_avg(Pomodoro, context['q_week'], context['q_week_end'])
        context['weight'] = Weight.get_week(Weight, context['q_week'], context['q_week_end'])
        context['steps'] = GoogleFit.get_week(GoogleFit, context['q_week'], context['q_week_end'])
        context['mood'] = Mood.get_week(Mood, context['q_week'], context['q_week_end'])
        context['week_num_now'] = datetime.datetime.now().isocalendar()[1]

        if context['q_week'] and context['q_week_end'] is not None:
            week = context['q_week'].split('-W')
            week_end = context['q_week_end'].split('-W')
            context['week'] = f'{week[1]}'
            context['week_end'] = f'{week_end[1]}'
        else:
            context['week'] = ''
            context['week_end'] = ''

        print(context['q_week'])
        print(context['q_week_end'])


        return context


class Selfdata_dashboard_month(TemplateView):
    template_name = "selfdata_dashboard_month.html"

    def get_context_data(self, **kwargs):
        context = super(Selfdata_dashboard_month, self).get_context_data(**kwargs)

        context['q_month'] = self.request.GET.get('q_month')
        context['q_month_end'] = self.request.GET.get('q_month_end')

        if context['q_month']is None:
            context['q_month'] = '2017-08'

        context['q_week'], context['q_week_end'] = month_to_week(context['q_month'], context['q_month_end'])
        # print(f"month: {context['q_week']}, {context['q_week_end']}")

        # print('selfdata_dashboard_month')
        # print(context['q_month'])
        # print(context['q_month_end'])




        context['slept_time'] = Sleep.get_week_sleep_total_hours_avg(Sleep, context['q_week'], context['q_week_end'])
        context['sleep'] = Sleep.get_week_sleep_total_hours(Sleep, context['q_week'], context['q_week_end'])
        context['pomodoro_total'] = Pomodoro.get_week_total(Pomodoro, context['q_week'], context['q_week_end'])
        context['pomodoro_per'] = Pomodoro.get_week_avg(Pomodoro, context['q_week'], context['q_week_end'])
        context['weight'] = Weight.get_week(Weight, context['q_week'], context['q_week_end'])
        context['steps'] = GoogleFit.get_week(GoogleFit, context['q_week'], context['q_week_end'])
        context['mood'] = Mood.get_week(Mood, context['q_week'], context['q_week_end'])
        context['week_num_now'] = datetime.datetime.now().isocalendar()[1]

        return context


class Selfdata_dashboard_month_2(TemplateView):
    template_name = "selfdata_dashboard_month_2.html"

    def get_context_data(self, **kwargs):
        context = super(Selfdata_dashboard_month_2, self).get_context_data(**kwargs)

        context['q_month'] = self.request.GET.get('q_month')
        context['q_month_end'] = self.request.GET.get('q_month_end')

        if context['q_month'] is None:
            if context['q_month_end'] is None:
                context['q_month'] = '2017-05'
                context['q_month_end'] = '2017-10'

        context['q_week'], context['q_week_end'] = month_to_week(context['q_month'], context['q_month_end'])
        # print(f"month_2: {context['q_week']}, {context['q_week_end']}")

        context['slept_time'] = Sleep.get_week_sleep_total_hours_avg(Sleep, context['q_week'], context['q_week_end'])
        context['sleep'] = Sleep.get_week_sleep_total_hours(Sleep, context['q_week'], context['q_week_end'])
        context['pomodoro_total'] = Pomodoro.get_week_total(Pomodoro, context['q_week'], context['q_week_end'])
        context['pomodoro_per'] = Pomodoro.get_week_avg(Pomodoro, context['q_week'], context['q_week_end'])
        context['weight'] = Weight.get_week(Weight, context['q_week'], context['q_week_end'])
        context['steps'] = GoogleFit.get_week(GoogleFit, context['q_week'], context['q_week_end'])
        context['mood'] = Mood.get_week(Mood, context['q_week'], context['q_week_end'])
        context['week_num_now'] = datetime.datetime.now().isocalendar()[1]

        return context
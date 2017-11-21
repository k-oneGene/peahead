"""peahead URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import (
    Selfdata_main,
    Selfdata_detail,
    Selfdata_dashboard,
    Selfdata_dashboard_week,
    Selfdata_dashboard_week_2,
    Selfdata_dashboard_month,
    Selfdata_dashboard_month_2
)


urlpatterns = [
    url(r'^$', Selfdata_main.as_view(), name='main'),
    url(r'^dashboard/$', Selfdata_dashboard.as_view(), name='dashboard'),
    url(r'^dashboard/week/$', Selfdata_dashboard_week.as_view(), name='dashboard_week'),
    url(r'^dashboard/week2/$', Selfdata_dashboard_week_2.as_view(), name='dashboard_week_2'),
    url(r'^dashboard/month/$', Selfdata_dashboard_month.as_view(), name='dashboard_month'),
    url(r'^dashboard/month2/$', Selfdata_dashboard_month_2.as_view(), name='dashboard_month_2'),
    url(r'^detail/(?P<slug>[\w-]+)$', Selfdata_detail.as_view(), name='detail'),
]

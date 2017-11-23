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
    Brainfood_main,
    Quotes_main,
    TrustTP_main,
    QuotesCreateView,
    QuotesListView,
    QuotesToday,
    QuotesRandom,
    QuotesUpdateView
)


urlpatterns = [
    url(r'^$', Brainfood_main.as_view(), name='main'),
    url(r'^quotes/$', Quotes_main.as_view(), name='quotes_main'),
    url(r'^quotes/create$', QuotesCreateView.as_view(), name='quotes_create'),
    url(r'^quotes/today$', QuotesToday.as_view(), name='quotes_today'),
    url(r'^quotes/all$', QuotesListView.as_view(), name='quotes_all'),
    url(r'^quotes/random$', QuotesRandom.as_view(), name='quotes_random'),
    url(r'^quotes/edit/(?P<pk>\d+)/$', QuotesUpdateView.as_view(), name='quotes_edit'),

    url(r'^trust/$', TrustTP_main.as_view(), name='trustTP_main'),

]

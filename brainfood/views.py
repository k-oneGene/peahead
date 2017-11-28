from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from django.urls import reverse

from .models import Quotes
from .forms import QuotesForm

# Create your views here.

class Brainfood_main(TemplateView):
    template_name = "brainfood_main.html"


class Quotes_main(TemplateView):
    template_name = "quotes_main.html"


class TrustTP_main(TemplateView):
    template_name = "trustTP_main.html"


class QuotesListView(ListView):
    model = Quotes
    template_name = 'quotes_list.html'


# When I have user model use "Last logged in date == Today, don't change. Else new quote.
class QuotesToday(TemplateView):
    template_name = 'quotes_today.html'

    def get_context_data(self, **kwargs):
        context = super(QuotesToday, self).get_context_data(**kwargs)


        context['todays_quote'] = Quotes.objects.order_by('?').first()
        print(context['todays_quote'])
        return context


class QuotesRandom(TemplateView):
    template_name = 'quotes_random.html'

    def get_context_data(self, **kwargs):
        context = super(QuotesRandom, self).get_context_data(**kwargs)
        quotes = Quotes()
        context['quote'] = quotes.get_random()

        return context


class QuotesCreateView(CreateView):
    form_class = QuotesForm
    template_name = 'form_quotes.html'
    # model = Quotes


class QuotesUpdateView(UpdateView):
    form_class = QuotesForm
    template_name = 'form_quotes.html'
    model = Quotes
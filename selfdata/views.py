from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.urls import reverse

from selfdata.Report.report_multiples import graph_report

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
        # For now instead of searching just return simple image
        q_start = self.request.GET.get('q_start')
        q_end = self.request.GET.get('q_end')
        print(q_start)
        print(q_end)
        print(kwargs['slug'])
        context['sd_type'] = kwargs['slug'] + '.svg'
        if q_start and q_end:
            graph_report(q_start, q_end)
            # run something to get data
        return context

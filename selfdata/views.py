from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse

# Create your views here.

# def home(request):
#     html = "<h1>Hello world</h1>"
#     return HttpResponse(html)


class Selfdata_main(TemplateView):
    template_name = "selfdata_main.html"
    # def get(self, request, *args, **kwargs):
    #     return render(request, )
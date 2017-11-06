from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse

# Create your views here.

class Brainfood_main(TemplateView):
    template_name = "brainfood_main.html"
    # def get(self, request, *args, **kwargs):
    #     return render(request, )
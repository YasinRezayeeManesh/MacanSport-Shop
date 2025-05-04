from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


# Create your views here.


class ServiceListView(ListView):
    model = models.Service
    template_name = 'service_module/service.html'
    context_object_name = 'services'
    paginate_by = 4


class ServiceDetailView(DetailView):
    model = models.Service
    template_name = 'service_module/service_detail.html'
    context_object_name = 'service'

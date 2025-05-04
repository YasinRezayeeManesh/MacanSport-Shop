from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models


# Create your views here.


class AboutUsView(TemplateView):
    template_name = 'about_us_module/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "about": models.AboutUs.objects.all().first(),
            "companies": models.Companies.objects.all(),
            'info_site': models.ContactUs.objects.all().first(),
        }
        return context


class TeamView(ListView):
    model = models.Team
    template_name = 'about_us_module/team_page.html'
    context_object_name = 'teams'

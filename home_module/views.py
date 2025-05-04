from django.shortcuts import render
from django.views.generic import TemplateView
from service_module.models import Service
from about_us_module.models import ContactUs, ManyInfo
from service_module.models import Service
from about_us_module.models import AboutUs, FrequentlyQuestions
from django.db.models import Count, Sum
from product_module.models import Product


# Create your views here.


class HomaPage(TemplateView):
    template_name = 'home_module/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info_site'] = ContactUs.objects.all().first()
        context['services'] = Service.objects.all()[:4]
        context['about'] = AboutUs.objects.all().first()
        context['questions'] = FrequentlyQuestions.objects.all()

        most_bought_product = Product.objects.filter(orderdetail__order__is_paid=True).annotate(order_count=Sum(
            'orderdetail__count'
        )).order_by('-order_count')[:8]
        context['most_bought_product'] = most_bought_product
        context['off_products'] = Product.objects.filter(off=True, inventory=True)[:8]

        return context


def site_header_component(request):
    context = {
        "info_site": ManyInfo.objects.all().first()
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    context = {
        "services": Service.objects.all(),
        "info_site": ContactUs.objects.all().first()
    }
    return render(request, 'shared/site_footer_component.html', context)

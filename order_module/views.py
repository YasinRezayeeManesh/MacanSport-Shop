from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from product_module.models import Product
from .models import *
from about_us_module.models import ManyInfo, ContactUs


# Create your views here.


def add_product_to_order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = int(request.GET.get('count'))
    if count < 1:
        return JsonResponse({
            'status': 'invalid count',
            'text': 'مقدار وارد شده نامعبتر میباشد',
            'title': 'خطا',
            'icon': 'error',
            'confirm_button_text': 'باشه ، ممنون',
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, inventory=True).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if not current_order.is_close:
                if current_order_detail is not None:
                    current_order_detail.count += count
                    current_order_detail.save()
                else:
                    new_detail = OrderDetail(product_id=product_id, count=count, order_id=current_order.id)
                    new_detail.save()
                return JsonResponse({
                    'status': 'success',
                    'text': 'محصول مورد نظر با موفقیت به سبد خرید شما افزوده شد',
                    'title': 'عملیات موفقیت آمیز بود',
                    'icon': 'success',
                    'confirm_button_text': 'باشه ، ممنون',
                })
            else:
                return JsonResponse({
                    'status': 'card close',
                    'text': 'کاربر گرامی سبد خرید شما بسته میباشد ، لطفا در ابتدا سبد خرید خود را کامل کنید',
                    'title': 'سبد خرید شما بسته میباشد',
                    'icon': 'error',
                    'confirm_button_text': 'باشه ، ممنون',
                })
        else:
            return JsonResponse({
                'status': 'not found',
                'text': 'محصول مورد نظر پیدا نشد',
                'title': 'خطا',
                'icon': 'error',
                'confirm_button_text': 'باشه ، ممنون',
            })
    else:
        return JsonResponse({
            'status': 'user is not authenticated',
            'text': 'لطفا در ابتدا وارد حساب کاربری خود در وبسایت شوید',
            'title': 'خطا',
            'icon': 'error',
            'confirm_button_text': 'ورود به حساب کاربری',
        })


def continue_payment(request: HttpRequest):
    current_order = Order.objects.filter(is_paid=False, user_id=request.user.id).first()
    current_order.is_close = True
    current_order.save()
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    context = {
        'total_amount': total_amount,
        'info_bank': ManyInfo.objects.all().first(),
        'info_site': ContactUs.objects.all().first(),
    }
    return render(request, 'order_module/continue_payment.html', context)

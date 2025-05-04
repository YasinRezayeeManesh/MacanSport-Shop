from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpRequest, JsonResponse
from account_module.models import User
from order_module.models import Order, OrderDetail
from .forms import EditUserPanelForm, ChangePasswordForm
from django.contrib.auth import logout
from about_us_module.models import ContactUs


# Create your views here.

@method_decorator(login_required, name='dispatch')
class UserPanelView(TemplateView):
    template_name = 'user_panel_module/panel_page.html'


@method_decorator(login_required, name='dispatch')
class EditUserPanelView(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditUserPanelForm(instance=current_user)
        context = {
            'form': edit_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/edit_panel_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditUserPanelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {
            'form': edit_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/edit_panel_page.html', context)


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    def get(self, request: HttpRequest):
        form = ChangePasswordForm()
        context = {
            'form': form,
        }
        return render(request, 'user_panel_module/change_password.html', context)

    def post(self, request: HttpRequest):
        current_user: User = User.objects.filter(id=request.user.id).first()
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data.get('current_password')
            if current_user.check_password(current_password):
                new_password = form.cleaned_data.get('new_password')
                current_user.set_password(new_password)
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))

            else:
                form.add_error('current_password', 'کلمه عبور فعلی اشتباه میباشد')
        context = {
            'form': form,
        }
        return render(request, 'user_panel_module/change_password.html', context)


class UserBasket(TemplateView):
    template_name = 'user_panel_module/user_basket_page.html'
    context_object_name = 'basket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                                 user_id=self.request.user.id)
        total_amount = current_order.calculate_total_price()

        context['order'] = current_order
        context['total_amount'] = total_amount
        context['info'] = ContactUs.objects.all().first()
        context['post_price'] = current_order.post_price()

        return context


def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'success': "detail_not_found_id",
        })

    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__is_paid=False, order__is_close=False,
                                                             order__user_id=request.user.id).delete()
    if deleted_count:
        return JsonResponse({
            'success': "detail_not_found",
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)

    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'total_amount': total_amount,
        'post_price': current_order.post_price()
    }
    return JsonResponse({
        'status': "success",
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })


def user_panel_menu_component(request):
    return render(request, 'user_panel_module/components/user_panel_component.html')


def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None:
        return JsonResponse({
            'status': 'not found detail or state'
        })
    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id,
                                              order__is_paid=False).first()

    if order_detail is None:
        return JsonResponse({
            'status': 'not found detail'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state invalid'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'total_amount': total_amount,
        'post_price': current_order.post_price()
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })

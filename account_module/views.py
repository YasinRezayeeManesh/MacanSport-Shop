from django.shortcuts import render
from django.views import View
from account_module.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from account_module.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
from utils.mail_service import send_email
from django.utils.crypto import get_random_string
from django.http import HttpRequest


# Create your views here.


class RegisterView(View):
    def get(self, request):
        context = {
            'register_form': RegisterForm()
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_first_name = register_form.cleaned_data.get('first_name')
            user_last_name = register_form.cleaned_data.get('last_name')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user_phone = register_form.cleaned_data.get('phone')
            user_address = register_form.cleaned_data.get('address')
            user: bool = User.objects.filter(email__iexact=user_email).exists()

            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری میباشد')
            else:
                new_user = User(
                    first_name=user_first_name,
                    last_name=user_last_name,
                    email=user_email,
                    email_active_code=get_random_string(48),
                    username=user_email,
                    mobile=user_phone,
                    address=user_address,
                    is_active=True,
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login_page'))

        context = {
            "register_form": register_form
        }
        return render(request, 'account_module/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                is_current_password = user.check_password(user_password)
                if is_current_password:
                    login(request, user)
                    return redirect(reverse('user_panel'))
                else:
                    login_form.add_error('password', 'رمز عبور اشتباه است!')
            else:
                login_form.add_error('email', 'شما حساب کاربری ندارید!')
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home_page'))


class ForgotPassView(View):
    def get(self, request):
        forgot_pass_form = ForgotPasswordForm()
        context = {
            'forgot_pass_form': forgot_pass_form
        }
        return render(request, 'account_module/forgot_pass_page.html', context)

    def post(self, request):
        forgot_pass_form = ForgotPasswordForm(request.POST)
        if forgot_pass_form.is_valid():
            user_email = forgot_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'email/forgot_pass.html')
                return redirect(reverse('home_page'))

        context = {
            'forgot_pass_form': forgot_pass_form
        }
        return render(request, 'account_module/forgot_pass_page.html', context)


class ResetPassView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('register_page'))

        context = {
            'reset_pass_form': ResetPasswordForm(),
            'user': user
        }
        return render(request, 'account_module/reset_pass_page.html', context)

    def post(self, request, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('register_page'))

            user_new_password = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(48)
            user.save()
            return redirect(reverse('login_page'))
        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'account_module/reset_pass_page.html', context)

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout_page'),
    path('forgot-pass/', views.ForgotPassView.as_view(), name='forgot_pass'),
    path('reset-pass/<active_code>', views.ResetPassView.as_view(), name='reset_pass'),
]

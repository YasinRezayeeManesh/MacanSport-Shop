from django.urls import path
from . import views


urlpatterns = [
    path('', views.AboutUsView.as_view(), name='about_us'),
    path('team', views.TeamView.as_view(), name='team'),
]

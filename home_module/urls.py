from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomaPage.as_view(), name='home_page'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.membership_plans, name='membership_plans'),
]
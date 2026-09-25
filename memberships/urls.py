from django.urls import path
from . import views


urlpatterns = [
    path('', views.membership_plans, name='membership_plans'),
     path('select/<int:plan_id>/', views.select_plan, name='select_plan'),
]
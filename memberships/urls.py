from django.urls import path
from . import views


urlpatterns = [
    path('', views.membership_plans, name='membership_plans'),
     path('select/<int:plan_id>/', views.select_plan, name='select_plan'),
     path(
    'checkout/<int:plan_id>/',
    views.create_checkout_session,
    name='create_checkout_session'
),
path(
    'success/',
    views.payment_success,
    name='payment_success'
),
]
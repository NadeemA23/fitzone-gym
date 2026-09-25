import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import MembershipPlan


def membership_plans(request):
    plans = MembershipPlan.objects.all()

    return render(
        request,
        'memberships/membership_plans.html',
        {'plans': plans}
    )
@login_required
def select_plan(request, plan_id):
    plan = get_object_or_404(MembershipPlan, id=plan_id)

    return render(
        request,
        'memberships/select_plan.html',
        {'plan': plan}
    )
@login_required
def create_checkout_session(request, plan_id):
    plan = get_object_or_404(MembershipPlan, id=plan_id)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': plan.name,
                    },
                    'unit_amount': int(plan.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri('/memberships/success/'),
        cancel_url=request.build_absolute_uri('/memberships/'),
    )

    return redirect(checkout_session.url)
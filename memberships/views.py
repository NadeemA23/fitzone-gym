import stripe
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import MembershipPlan, UserMembership


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
        client_reference_id=str(request.user.id),
        metadata={'plan_id': str(plan.id)}, 
       success_url=request.build_absolute_uri(
    '/memberships/success/?session_id={CHECKOUT_SESSION_ID}'
),
cancel_url=request.build_absolute_uri('/memberships/'),
       )

    return redirect(checkout_session.url)

@login_required
def payment_success(request):
    session_id = request.GET.get('session_id')

    if not session_id:
        return redirect('membership_plans')

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.retrieve(session_id)

    if checkout_session.payment_status != 'paid':
        return redirect('membership_plans')

    if str(checkout_session.client_reference_id) != str(request.user.id):
        return redirect('membership_plans')

    if UserMembership.objects.filter(
        stripe_session_id=session_id
    ).exists():
        return redirect('dashboard')
    

    with transaction.atomic():
        membership, created = UserMembership.objects.select_for_update().get_or_create(
            user=request.user,
            defaults={
                'plan': plan,
                'start_date': start_date,
                'end_date': end_date,
                'active': True,
                'stripe_session_id': session_id,
            }
        )

        if not created and membership.stripe_session_id != session_id:
            membership.plan = plan
            membership.start_date = start_date
            membership.end_date = end_date
            membership.active = True
            membership.stripe_session_id = session_id
            membership.save()
        

    return render(
        request,
        'memberships/payment_success.html',
        {'plan': plan}
    )
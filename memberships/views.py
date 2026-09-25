import stripe
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
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
       success_url='https://bookish-happiness-57wg9vj5rvj26w5-8000.app.github.dev/memberships/success/?session_id={CHECKOUT_SESSION_ID}',
       cancel_url='https://bookish-happiness-57wg9vj5rvj26w5-8000.app.github.dev/memberships/',
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

    plan_id = checkout_session.metadata['plan_id']
    plan = get_object_or_404(MembershipPlan, id=plan_id)

    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=plan.duration_days)

    UserMembership.objects.update_or_create(
        user=request.user,
        defaults={
            'plan': plan,
            'start_date': start_date,
            'end_date': end_date,
            'active': True,
        }
    )

    return render(
        request,
        'memberships/payment_success.html',
        {'plan': plan}
    )
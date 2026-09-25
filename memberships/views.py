from django.shortcuts import render, get_object_or_404
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
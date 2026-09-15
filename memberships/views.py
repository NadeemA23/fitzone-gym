from django.shortcuts import render
from .models import MembershipPlan


def membership_plans(request):
    plans = MembershipPlan.objects.all()

    return render(
        request,
        'memberships/membership_plans.html',
        {'plans': plans}
    )
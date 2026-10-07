from django.shortcuts import render
from .models import GymClass


def class_list(request):
    gym_classes = GymClass.objects.all().order_by('date', 'time')

    return render(
        request,
        'classes/class_list.html',
        {'gym_classes': gym_classes}
    )
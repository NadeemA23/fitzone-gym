from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import GymClass, Booking
from django.contrib import messages


def class_list(request):
    gym_classes = GymClass.objects.all().order_by('date', 'time')

    return render(
        request,
        'classes/class_list.html',
        {'gym_classes': gym_classes}
    )
@login_required
def book_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)

    Booking.objects.get_or_create(
        user=request.user,
        gym_class=gym_class
    )

    messages.success(
        request,
        f"You have booked {gym_class.name}."
    )

    return redirect('class_list')
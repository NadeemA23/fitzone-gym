from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import GymClass, Booking


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

    booking, created = Booking.objects.get_or_create(
        user=request.user,
        gym_class=gym_class
    )

    if created:
        messages.success(
            request,
            f"You have booked {gym_class.name}."
        )
    else:
        messages.info(
            request,
            f"You have already booked {gym_class.name}."
        )

    return redirect('class_list')


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if request.method == 'POST':
        booking.delete()
        messages.success(
            request,
            "Your booking has been cancelled."
        )

    return redirect('dashboard')
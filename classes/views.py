from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import GymClass, Booking
from django.contrib.admin.views.decorators import staff_member_required
from .forms import GymClassForm
from django.utils import timezone
from memberships.models import UserMembership

def class_list(request):
    gym_classes = GymClass.objects.all().order_by('date', 'time')

    return render(
        request,
        'classes/class_list.html',
        {'gym_classes': gym_classes}
    )


@login_required
@require_POST
def book_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)

    has_membership = UserMembership.objects.filter(
        user=request.user,
        active=True,
        end_date__gte=timezone.localdate()
    ).exists()

    if not has_membership:
        messages.error(
            request,
            "You need an active gym membership to book classes."
        )
        return redirect('class_list')

    if Booking.objects.filter(
        user=request.user,
        gym_class=gym_class
    ).exists():
        messages.info(request, "You have already booked this class.")
        return redirect('class_list')

    current_bookings = Booking.objects.filter(
        gym_class=gym_class
    ).count()

    if current_bookings >= gym_class.capacity:
        messages.error(request, "Sorry, this class is fully booked.")
        return redirect('class_list')

    Booking.objects.create(
        user=request.user,
        gym_class=gym_class
    )

    messages.success(
        request,
        f"You have booked {gym_class.name}."
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

@staff_member_required
def add_class(request):
    if request.method == 'POST':
        form = GymClassForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Gym class added successfully.")
            return redirect('class_list')
    else:
        form = GymClassForm()

    return render(
        request,
        'classes/class_form.html',
        {'form': form, 'page_title': 'Add Gym Class'}
    )
@staff_member_required
def edit_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)

    if request.method == 'POST':
        form = GymClassForm(request.POST, instance=gym_class)

        if form.is_valid():
            form.save()
            messages.success(request, "Gym class updated successfully.")
            return redirect('class_list')
    else:
        form = GymClassForm(instance=gym_class)

    return render(
        request,
        'classes/class_form.html',
        {
            'form': form,
            'page_title': 'Edit Gym Class'
        }
    )
@staff_member_required
def delete_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)

    if request.method == 'POST':
        gym_class.delete()
        messages.success(request, "Gym class deleted successfully.")
        return redirect('class_list')

    return render(
        request,
        'classes/class_confirm_delete.html',
        {'gym_class': gym_class}
    )
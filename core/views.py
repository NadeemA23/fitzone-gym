from django.shortcuts import render


def home(request):
    """Display the FitZone Gym homepage."""
    return render(request, 'core/home.html')
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from memberships.models import UserMembership

def home(request):
    """Display the FitZone Gym homepage."""
    return render(request, 'core/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(
        request,
        'core/register.html',
        {'form': form}
    )

@login_required
def dashboard(request):
    try:
        membership = UserMembership.objects.get(user=request.user)
    except UserMembership.DoesNotExist:
        membership = None

    return render(
        request,
        'core/dashboard.html',
        {'membership': membership}
    )
   
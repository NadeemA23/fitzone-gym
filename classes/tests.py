from django.contrib.auth.models import User
from .models import Booking
from .models import GymClass
from .forms import GymClassForm
from django.test import TestCase
from django.urls import reverse
from memberships.models import MembershipPlan, UserMembership
from django.utils import timezone
from datetime import timedelta

class GymClassTests(TestCase):

    def test_class_list_page_loads(self):
        response = self.client.get(
            reverse('class_list'),
            secure=True
        )
        self.assertEqual(response.status_code, 200)

    def test_gym_class_can_be_created(self):
        gym_class = GymClass.objects.create(
            name="Test Boxing",
            description="A beginner boxing class",
            instructor="Alex",
            date="2026-11-20",
            time="14:00",
            capacity=10
        )

        self.assertEqual(gym_class.name, "Test Boxing")
        self.assertEqual(gym_class.capacity, 10)
        self.assertEqual(GymClass.objects.count(), 1)

    def test_capacity_cannot_be_zero(self):
        form = GymClassForm(data={
            'name': 'Test Boxing',
            'description': 'Beginner boxing class',
            'instructor': 'Alex',
            'date': '2026-11-20',
            'time': '14:00',
            'capacity': 0
        })

        self.assertFalse(form.is_valid())
        self.assertIn('capacity', form.errors)

    def test_user_without_membership_cannot_book(self):
        user = User.objects.create_user(
            username="testmember",
            password="TestPassword123!"
        )

        gym_class = GymClass.objects.create(
            name="Test Boxing",
            description="Beginner boxing class",
            instructor="Alex",
            date="2026-11-20",
            time="14:00",
            capacity=10
        )

        self.client.force_login(user)

        response = self.client.post(
            reverse('book_class', args=[gym_class.id]),
            secure=True
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Booking.objects.filter(
                user=user,
                gym_class=gym_class
            ).exists()
        )

    def test_user_cannot_book_same_class_twice(self):
        user = User.objects.create_user(
            username="duplicatetest",
            password="TestPassword123!"
        )

        plan = MembershipPlan.objects.create(
            name="Monthly Membership",
            description="One month gym access",
            price="29.99",
            duration_days=30
        )

        today = timezone.localdate()

        UserMembership.objects.create(
            user=user,
            plan=plan,
            start_date=today,
            end_date=today + timedelta(days=30),
            active=True
        )

        gym_class = GymClass.objects.create(
            name="Test Boxing",
            description="Beginner boxing class",
            instructor="Alex",
            date=today + timedelta(days=7),
            time="14:00",
            capacity=10
        )

        self.client.force_login(user)

        booking_url = reverse(
            'book_class',
            args=[gym_class.id]
        )

        self.client.post(booking_url, secure=True)
        self.client.post(booking_url, secure=True)

        self.assertEqual(
            Booking.objects.filter(
                user=user,
                gym_class=gym_class
            ).count(),
            1
        )
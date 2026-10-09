from django import forms
from .models import GymClass


class GymClassForm(forms.ModelForm):
    class Meta:
        model = GymClass
        fields = [
            'name',
            'description',
            'instructor',
            'date',
            'time',
            'capacity'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_capacity(self):
        capacity = self.cleaned_data['capacity']

        if capacity < 1:
            raise forms.ValidationError(
                "Class capacity must be at least 1."
            )

        return capacity
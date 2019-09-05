from django import forms
from .models import Exercises

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercises
        fields =[
            "exercise",
            "reps",
        ]
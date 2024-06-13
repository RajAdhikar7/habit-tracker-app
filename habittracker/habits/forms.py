from django import forms
from.models import Habit , HabitEvent

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        # fields of the form
        fields = ['name','description','difficulty']


class HabitCompletionForm(forms.ModelForm):
    class Meta:
        model = HabitEvent
        fields = ['date']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}
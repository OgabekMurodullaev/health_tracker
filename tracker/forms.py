from django import forms
from .models import MoodEntry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'stress_level', 'sleep_quality', 'note']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Saqlash'))

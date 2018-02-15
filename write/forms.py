from django import forms
from .models import Wave


class WaveForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ('money', 'description')

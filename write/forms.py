from django import forms
from .models import Wave
from mainapp.models import Profile


class WaveForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ('money', 'description')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('balance',)

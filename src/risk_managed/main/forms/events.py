from django import forms

from risk_managed.main.models import Event, GuestImage


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'host': forms.HiddenInput()
        }

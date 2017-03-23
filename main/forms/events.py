from django import forms

from main.models import Event, GuestImage


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'host': forms.HiddenInput()
        }

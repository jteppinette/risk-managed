from django import forms

from risk_managed.main.models import Flag


class FlagForm(forms.ModelForm):
    class Meta:
        model = Flag
        fields = '__all__'
        widgets = {
            'guest': forms.HiddenInput(),
            'host': forms.HiddenInput(),
            'administrator': forms.HiddenInput()
        }

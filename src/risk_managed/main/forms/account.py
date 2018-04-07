from django import forms
from django.contrib.auth.models import User


class EmailChangeForm(forms.Form):
    email = forms.EmailField()

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists.")
            
        return self.cleaned_data

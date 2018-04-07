from django import forms

genders = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class GuestForm(forms.Form):
    date_of_birth = forms.DateField(widget = forms.TextInput(attrs={'type': 'date','placeholder': 'Date of Birth'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Last name'}))
    gender = forms.ChoiceField(choices=genders)
    photo = forms.ImageField()

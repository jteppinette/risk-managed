from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from main.models import University, Organization, Host, Administrator


class RegisterHostForm(UserCreationForm):
    organization = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'What is your national organization eg. Kappa Sigma'}), max_length=80)
    university = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Your School eg. University of Georgia'}), max_length=80)

    class Meta:
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields + ('organization', 'university', 'email')

    def save(self):
        user = super(RegisterHostForm, self).save()
        organization = Organization.objects.get(name__iexact=self.cleaned_data.get('organization'))
        university = University.objects.get(name__iexact=self.cleaned_data.get('university'))
        host = Host(user=user, organization=organization, university=university)
        host.save()
        return user

    def clean(self):
        cleaned_data = super(RegisterHostForm, self).clean()
        university = cleaned_data.get('university')
        organization = cleaned_data.get('organization')
        
        if Host.objects.filter(university__name=university, organization__name=organization).exists():
            raise forms.ValidationError("There is already an account with that organization and school combination. Contact us at support@riskmanaged.org")
            
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The provided email already exists.")
        return email

    def clean_university(self):
        university = self.cleaned_data.get('university')
        if not University.objects.filter(name=university).exists():
            raise forms.ValidationError("The provided university does not exist.")
        return university

    def clean_organization(self):
        organization = self.cleaned_data.get('organization')
        if not Organization.objects.filter(name=organization).exists():
            raise forms.ValidationError("The provided organization does not exist.")
        return organization


class RegisterAdministratorForm(UserCreationForm):
    university = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'University you are an administrator of eg. University of Georgia'}), max_length=80)

    class Meta:
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields + ('university', 'email')

    def save(self):
        user = super(RegisterAdministratorForm, self).save()
        university = University.objects.get(name__iexact=self.cleaned_data.get('university'))
        administrator = Administrator(user=user, university=university)
        administrator.save()
        return user

    def clean(self):
        cleaned_data = super(RegisterAdministratorForm, self).clean()
        university = cleaned_data.get('university')
        
        if Administrator.objects.filter(university__name=university).exists():
            raise forms.ValidationError("There is already an administrator for this University. Contact us at support@riskmanaged.org")
            
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The provided email already exists.")
        return email

    def clean_university(self):
        university = self.cleaned_data.get('university')
        if not University.objects.filter(name=university).exists():
            raise forms.ValidationError("The provided university does not exist.")
        return university

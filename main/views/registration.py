from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from main.models import Host, Organization, University, Administrator
from main.forms import RegisterHostForm, RegisterAdministratorForm

def host(request):
    if request.method == 'POST':
        form = RegisterHostForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterHostForm()
    return render(request, 'registration/host.html', {
        'form': form,
    })
    
def administrator(request):
    if request.method == 'POST':
        form = RegisterAdministratorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterAdministratorForm()
    return render(request, 'registration/administrator.html', {
        'form': form,
    })

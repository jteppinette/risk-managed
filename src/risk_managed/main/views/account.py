from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from risk_managed.main.forms import EmailChangeForm

@login_required
def manage(request):
    return render(request, 'account/manage.html')

@login_required
def email_change(request):
    if request.method == 'POST':
        form = EmailChangeForm(data=request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect('account_manage')
    else:
        form = EmailChangeForm()

    return render(request, 'account/email_change.html', {
        'form': form,
    })

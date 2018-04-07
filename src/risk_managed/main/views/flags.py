from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from risk_managed.main.models import Flag, Guest
from risk_managed.main.forms import FlagForm

def list(request):
    host_flags = Flag.objects.filter(host__in=request.user.administrator.host_set.all())
    admin_flags = Flag.objects.filter(administrator=request.user.administrator)
    return render(request, 'flags/list.html', {
        'host_flags': host_flags,
        'admin_flags': admin_flags,
    })

@login_required
def delete(request, flag):
    flag = get_object_or_404(Flag, pk=flag)
    guest = flag.guest
    flag.delete()
    if hasattr(request.user, 'administrator'):
        if 'guests' in request.META.get('HTTP_REFERER'):
            return redirect('guests_detail', guest.pk)
        else:
            return redirect('flags_list')
    else:
        return redirect('guests_detail', guest.pk)

@login_required
def new(request, guest):
    guest = get_object_or_404(Guest, pk=guest)
    if request.method == 'POST':
        data = request.POST.dict()
        data['guest'] = guest.pk
        if hasattr(request.user, 'administrator'):
            data['administrator'] = request.user.administrator.pk
        if hasattr(request.user, 'host'):
            data['host'] = request.user.host.pk
        form = FlagForm(data)
        if form.is_valid():
            form.save()
            return redirect('guests_detail', guest.pk)
    else:
        form = FlagForm()

    return render(request, 'flags/new.html', {
        'form': form,
    })

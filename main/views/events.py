from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import utc
from django.conf import settings

import datetime
import os

from main.models import Event, GuestImage, Guest
from main.forms import EventForm, GuestForm

@login_required
def list(request):
    if hasattr(request.user, 'host'):
        events = Event.objects.filter(host__exact=request.user.host).order_by('-date_of_event',)
    else:
        events = Event.objects.filter(host__in=request.user.administrator.host_set.all()).order_by('-date_of_event')

    return render(request, 'events/list.html', {
        'events': events,
    })

@login_required
def detail(request, event):
    event = get_object_or_404(Event, pk=event)
    guestimages = GuestImage.objects.filter(event=event).order_by('-date_time_taken')
    return render(request, 'events/detail.html', {
        'event': event,
        'guestimages': guestimages
    })

@login_required
def new(request):
    if request.method == 'POST':
        data = request.POST.dict()
        data['host'] = request.user.host.pk
        form = EventForm(data)
        if form.is_valid():
            form.save()
            return redirect('events_list')
    else: 
        form = EventForm()
    return render(request, 'events/new.html', {
        'form': form,
    })

@login_required
def checkin(request, event):
        event = get_object_or_404(Event, pk=event)
        if request.method == 'POST':
            form = GuestForm(request.POST, request.FILES)
            if form.is_valid():
                date_of_birth = form.cleaned_data['date_of_birth']
                first_name = form.cleaned_data['first_name'].strip()
                last_name = form.cleaned_data['last_name'].strip()
                gender = form.cleaned_data['gender']

                guests = Guest.objects.filter(date_of_birth=date_of_birth, first_name__iexact=first_name, last_name__iexact=last_name)
                if not guests:
                    guest = Guest(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, gender=gender)
                    guest.save()
                else:
                    guest = guests[0]

                if not guest.event.all().filter(pk=event.pk).exists():
                    guest.event.add(event)
                    name, ext = os.path.splitext(request.FILES['photo'].name)
                    relative_file_path = os.path.join('images', 'guests', str(guest.pk) + '-' + str(event.pk) + ext)
                    absolute_file_path = os.path.join(settings.MEDIA_ROOT, relative_file_path)
                    if not os.path.isdir(os.path.dirname(absolute_file_path)):
                        os.makedirs(os.path.dirname(absolute_file_path))
                    with open(absolute_file_path, 'wb+') as destination:
                        for chunk in request.FILES['photo'].chunks():
                            destination.write(chunk)
                    guestimage = GuestImage(image=relative_file_path, image_thumb=relative_file_path, guest=guest, event=event, date_time_taken=datetime.datetime.utcnow().replace(tzinfo=utc))
                    guestimage.save()

                return redirect('events_detail', event.pk)
        else: 
            form = GuestForm()

        return render(request, 'events/checkin.html', {
            'form': form,
            'event': event,
        })

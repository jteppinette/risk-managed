from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from main.models import Event

@login_required
def events_list(request, host):
    events = Event.objects.filter(host=host).order_by('-date_of_event')
    return render(request, 'events/list.html', {
        'events': events,
    })

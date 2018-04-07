from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from risk_managed.main.models import Event, GuestImage, Guest


class List(LoginRequiredMixin, ListView):
    template_name = 'guests/list.html'
    model = GuestImage

    def get_queryset(self, *args, **kwargs):
        if hasattr(self.request.user, 'administrator'):
            events = Event.objects.filter(host__in=self.request.user.administrator.host_set.all())
        else:
            events = Event.objects.filter(host__user__exact=self.request.user)

        return GuestImage.objects.filter(event__in=events).order_by('guest__last_name', 'guest__first_name').distinct()


class Detail(LoginRequiredMixin, DetailView):
    template_name = 'guests/detail.html'
    model = Guest

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if hasattr(self.request.user, 'administrator'):
            hosts = self.request.user.administrator.host_set.all()
            context['guestimages'] = GuestImage.objects.filter(event__host__in=hosts, guest=self.get_object()).order_by('-date_time_taken')
        else:
            context['guestimages'] = GuestImage.objects.filter(event__host=self.request.user.host, guest=self.get_object()).order_by('-date_time_taken')

        return context

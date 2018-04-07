from django.conf.urls import url, include
from django.contrib import admin

from risk_managed.main.views import guests, terms, privacy, dashboard, home, account, events, hosts, flags, registration

urlpatterns = [
    url('^$', home.view, name='home'),
    url('^dashboard/$', dashboard.view, name='dashboard'),
    url('^terms/$', terms.view, name='terms'),
    url('^privacy/$', privacy.view, name='privacy'),

    url('^register-host$', registration.host, name='register_host'),
    url('^register-administrator$', registration.administrator, name='register_administrator'),
    
    url('^events/$', events.list, name='events_list'),
    url('^events/new/$', events.new, name='events_new'),
    url('^events/(?P<event>\d+)/$', events.detail, name='events_detail'),
    url('^events/(?P<event>\d+)/checkin/$', events.checkin, name='events_checkin'),
    
    url('^hosts/(?P<host>\d+)/events/$', hosts.events_list, name='hosts_events_list'),
    
    url('^guests/$', guests.List.as_view(), name='guests_list'),
    url('^guests/(?P<pk>\d+)/$', guests.Detail.as_view(), name='guests_detail'),
    url('^guests/(?P<guest>\d+)/flags/new/$', flags.new, name='flags_new'),

    url('^flags/(?P<flag>\d+)/delete/$', flags.delete, name='flags_delete'),
    url('^flags/$', flags.list, name='flags_list'),
    
    url('^account', account.manage, name='account_manage'),
    url('^email_change$', account.email_change, name='account_email_change'),

    url('^', include('django.contrib.auth.urls')),
    url('^admin/', admin.site.urls),
]

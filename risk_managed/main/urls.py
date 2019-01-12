from django.contrib import admin
from django.urls import include, path

from risk_managed.main.views import (
    account,
    dashboard,
    events,
    flags,
    guests,
    home,
    hosts,
    privacy,
    registration,
    terms,
)

urlpatterns = [
    path("dashboard", dashboard.view, name="dashboard"),
    path("", home.view, name="home"),
    path("", include("django.contrib.auth.urls")),
    path("terms", terms.view, name="terms"),
    path("privacy", privacy.view, name="privacy"),
    path("register-host", registration.host, name="register_host"),
    path("register-administrator", registration.administrator, name="register_administrator"),
    path("events", events.list, name="events_list"),
    path("events/new", events.new, name="events_new"),
    path("events/<int:event>", events.detail, name="events_detail"),
    path("events/<int:event>/checkin", events.checkin, name="events_checkin"),
    path("hosts/<int:host>/events", hosts.events_list, name="hosts_events_list"),
    path("guests", guests.List.as_view(), name="guests_list"),
    path("guests/<int:pk>", guests.Detail.as_view(), name="guests_detail"),
    path("guests/<int:guest>/flags/new", flags.new, name="flags_new"),
    path("flags/<int:flag>/delete", flags.delete, name="flags_delete"),
    path("flags", flags.list, name="flags_list"),
    path("account", account.manage, name="account_manage"),
    path("email_change", account.email_change, name="account_email_change"),
    path("admin", admin.site.urls),
]

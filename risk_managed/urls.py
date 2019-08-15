from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.urls import path

from risk_managed.views import (
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
    path("email-change", account.email_change, name="account_email_change"),
    path("admin", admin.site.urls),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("password-change", PasswordChangeView.as_view(), name="password_change"),
    path("password-change-done", PasswordChangeDoneView.as_view(), name="password_change_done"),
]

from django.contrib import admin

from risk_managed.main.models import (
    Administrator,
    Event,
    Flag,
    Guest,
    GuestImage,
    Host,
    Organization,
    University,
)


class OrganizationAdmin(admin.ModelAdmin):
    pass


class UniversityAdmin(admin.ModelAdmin):
    pass


class GuestImageInline(admin.TabularInline):
    extra = 2
    model = GuestImage


class EventInline(admin.TabularInline):
    extra = 1
    model = Event


class FlagInline(admin.TabularInline):
    extra = 1
    model = Flag


class FlagAdmin(admin.ModelAdmin):
    list_display = ("guest", "priority", "category")


class GuestAdmin(admin.ModelAdmin):
    list_display = ("__str__", "gender")
    search_fields = ["last_name", "first_name"]
    inlines = [GuestImageInline, FlagInline]


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "host_email")


class AdministratorAdmin(admin.ModelAdmin):
    list_display = ("user_email", "university")


class HostAdmin(admin.ModelAdmin):
    list_display = ("user_email", "university", "organization", "has_admin")
    inlines = [EventInline]


class GuestImageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "event_name", "date_time_taken")


admin.site.register(Host, HostAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(GuestImage, GuestImageAdmin)
admin.site.register(Flag, FlagAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Organization, OrganizationAdmin)

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "location", "url", "birthday")
    search_fields = ("user__username", "location", "url")
    list_filter = ("birthday",)
    date_hierarchy = "birthday"

    fieldsets = (
        ("User Info", {
            "fields": ("user",)
        }),
        ("Profile Details", {
            "fields": ("banner", "location", "url", "birthday", "profile_info")
        }),
        ("Social Media", {
            "fields": ("twitter", "instagram", "linkedin", "youtube", "github")
        }),
    )


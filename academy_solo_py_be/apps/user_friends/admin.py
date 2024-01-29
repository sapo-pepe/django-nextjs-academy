# Register your models here.
from django.contrib import admin
from .models import FriendRequest, FriendList


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ("from_user", "to_user", "timestamp", "is_archived", "is_accepted")
    list_filter = ("is_archived", "is_accepted")
    search_fields = ("from_user__username", "to_user__username")
    date_hierarchy = "timestamp"


admin.site.register(FriendRequest, FriendRequestAdmin)


class FriendListAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username",)
    filter_horizontal = ("friends",)


admin.site.register(FriendList, FriendListAdmin)

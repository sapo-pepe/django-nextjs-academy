from django.contrib import admin
from .models import (
    SellerContact,
    InstructorContact,
    FriendContact,
    SellerContactList,
    InstructorContactList,
    FriendContactList,
)
# Register your models here.


@admin.register(SellerContact, InstructorContact, FriendContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("user", "contact", "date_created")
    search_fields = ("user__username", "contact__username")


@admin.register(SellerContactList, InstructorContactList, FriendContactList)
class ContactListAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username",)

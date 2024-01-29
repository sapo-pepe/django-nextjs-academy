from django.db import models
from django.contrib import admin
from django.conf import settings
from djoser.signals import user_registered

# Create your models here.

User = settings.AUTH_USER_MODEL


class Contact(models.Model):
    # %(class)  refers to a string substitution that will be automatically filled with the model class name.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_contacts")
    contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_contacted_by")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        unique_together = ("user", "contact")


class SellerContact(Contact):
    class Meta:
        verbose_name_plural = 'Seller Contacts'


class InstructorContact(Contact):
    class Meta:
        verbose_name_plural = 'Instructor Contacts'


class FriendContact(Contact):
    class Meta:
        verbose_name_plural = 'Friend Contacts'


class SellerContactList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(SellerContact, blank=True)

    def __str__(self):
        return self.user.username + "'s Seller Contacts"


class InstructorContactList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(InstructorContact, blank=True)

    def __str__(self):
        return self.user.username + "'s Seller Contacts"


class FriendContactList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(FriendContact, blank=True)

    def __str__(self):
        return self.user.username + "'s Seller Contacts"


def post_user_registered(request, user, *args, **kwargs):
    # 1. Define register user

    user = user
    FriendContactList.objects.create(user=user)
    InstructorContact.objects.create(user=user)
    SellerContactList.objects.create(user=user)


user_registered.connect(post_user_registered)

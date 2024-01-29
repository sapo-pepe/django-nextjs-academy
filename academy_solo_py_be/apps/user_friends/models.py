from django.db import models
from django.conf import settings
from djoser.signals import user_registered
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

User = settings.AUTH_USER_MODEL


class FriendRequest(models.Model):
    # You will be able to access friend requests sent by a specific user through this inverse relationship
    from_user = models.ForeignKey(User, related_name="friend_requests_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="friend_request_recived", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # if the user doesnt accept the friend's request it gets archived
    is_archived = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)

    # The unique_together option is used to ensure that the combination of values in the specified fields is unique in the database. In this case, you are declaring that the combination of from_user and to_user must be unique, meaning that there cannot be two records in the database with the same value in both fields.
    # In practical terms, this translates to not being able to have multiple friend requests between the same users. For example, if there is already a friend request from User A to User B, you cannot create another friend request from User A to User B without first deleting the existing request.
    class Meta:
        unique_together = ("from_user", "to_user")


class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="friend_list")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username


def post_user_registered(request, user, *args, **kwargs):
    # 1 Defined registering  user
    user = user

    FriendList.objects.create(user=user)


user_registered.connect(post_user_registered)

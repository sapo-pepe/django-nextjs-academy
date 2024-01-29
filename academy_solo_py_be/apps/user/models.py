from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from slugify import slugify
import uuid
from django.utils import timezone

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # def create_slug(username):
        #     # This is a regex validation in order the user do not create strages slugs
        #     patter_special_characters = '\badmin\b|[!@#$%^~&*()_+==[]{}|;:",.<>/?]|\s'
        #     if re.search(patter_special_characters):
        #         raise ValueError('Username contains invalid characters')
        #     username = re.sub(patter_special_characters, '', username)
        #     return slugify(username)

        if not email:
            raise ValueError('Users must been an email address')

        email = self.normalize_email(email)
        # extra_fields['slug'] = create_slug(extra_fields['username'])
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.role = 'Admin'
        user.verified = True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    roles = (
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('helper', 'Helper'),
        ('editor', 'Editor'),
        ('owner', 'Owner'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    picture = models.ImageField(default='media/users/user_default_profile.png', upload_to='media/users/pictures/')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_online = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    role = models.CharField(max_length=20, choices=roles, default='customer')
    verified = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
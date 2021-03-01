from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from api.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='username',
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
    )
    role = models.CharField(
        max_length=10,
        verbose_name='Роль пользователя',
        choices=Role.choices,
        default=Role.USER
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        null=True
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        null=True
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True
    )
    is_staff = models.BooleanField(verbose_name='is_staff', default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    # class Meta:
     #   ordering = ['username']


class TempAuth(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
    )
    conf_code = models.CharField(
        max_length=62,
        verbose_name='confirmation code',
    )
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']

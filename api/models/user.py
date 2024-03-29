from api.managers import UserManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


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
    is_staff = models.BooleanField(
        verbose_name='is_staff',
        default=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_role_admin(self):
        return self.role == 'admin'

    @property
    def is_role_moderator(self):
        return self.role == 'moderator'


class TempAuth(models.Model):
    email = models.EmailField(
        max_length=254,
        verbose_name='email address',
        unique=True,
    )
    conf_code = models.CharField(
        max_length=62,
        verbose_name='confirmation code',
    )

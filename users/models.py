from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=50, unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    last_login = models.DateTimeField(
        default=datetime.now,
        verbose_name="Дата последнего посещения",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(null=True, blank=True)
    tg_chat_id = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Телеграм chat_id",
        help_text="Укажите телеграм chat_id",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

from django.db import models
from django.contrib.auth.models import AbstractUser


class ToDoListUser(AbstractUser):
    """Модель пользователя"""
    telegram_id = models.CharField(verbose_name="Телеграм пользователя", max_length=150, default="None")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


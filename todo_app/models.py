from django.db import models
from users.models import ToDoListUser


class Task(models.Model):
    """Модель задач"""
    user = models.ForeignKey(ToDoListUser, verbose_name="Автор задачи", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название задачи", max_length=150)
    description = models.CharField(verbose_name="Описание задачи", max_length=500)
    complete = models.BooleanField(default=False, verbose_name="Выполнена?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title

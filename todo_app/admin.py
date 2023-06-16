from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Отображение полей в админке"""
    list_display = ('user', 'title', 'description', 'complete')
    search_fields = ('user', 'title', 'description', 'complete')


admin.site.register(Task, TaskAdmin)

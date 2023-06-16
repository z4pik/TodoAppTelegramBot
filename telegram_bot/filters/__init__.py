from aiogram import Dispatcher

from .private_chat import IsPrivate


# Функция, которая выполняет установку кастомных фильтров
def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)  # Устанавливает кастомный фильтр на приватный чат с ботом

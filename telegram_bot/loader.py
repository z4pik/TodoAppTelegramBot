from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Создаём переменную бота


bot = Bot(token='6134156257:AAE_u7QZFUqocu2zi6dCtRRP5J9RyUNf3Uw', parse_mode=types.ParseMode.HTML)

# Создаем хранилище в оперативной памяти
storage = MemoryStorage()
# Создаем диспетчер
dp = Dispatcher(bot, storage=storage)

__all__ = ['bot', 'storage', 'dp']

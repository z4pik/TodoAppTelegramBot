from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('get_telegram_id'))  # /get_telegram_id
async def create_task_(message: types.Message):
    await message.answer(f'Привет! Знакомься твой telegram ID - {str(message.from_user.id)}')

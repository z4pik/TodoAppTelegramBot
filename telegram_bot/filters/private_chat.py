from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


# Фильтр, который отвечает за выполнения handler`а -
# Если чат приватный
class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states import create_task

import os
import django
from asgiref.sync import sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from todo_app.models import ToDoListUser, Task


@dp.message_handler(Command('create_task'))  # /create_task
async def create_task_(message: types.Message):
    telegram_id = str(message.from_user.id)

    try:
        user = await sync_to_async(ToDoListUser.objects.get)(telegram_id=telegram_id)
        await message.answer('Привет, ты решил создать новую задачу.\nПридумай ей название)', )
        await create_task.test1.set()
    except ToDoListUser.DoesNotExist:
        await message.answer('Ты не зарегистрирован. Пожалуйста, зарегистрируйся сначала.')


@dp.message_handler(state=create_task.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('Прекрасное название. Теперь описание')
    await create_task.test2.set()


@dp.message_handler(state=create_task.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await state.get_data()
    title = data.get('test1')
    description = data.get('test2')

    telegram_id = str(message.from_user.id)

    try:
        user = await sync_to_async(ToDoListUser.objects.get)(telegram_id=telegram_id)
        task = await sync_to_async(Task.objects.create)(user=user, title=title, description=description)
        await message.answer(f'Задача успешно создана\n'
                             f'Название: {title}\n'
                             f'Описание: {description}')
        await state.finish()
    except ToDoListUser.DoesNotExist:
        await message.answer('Ты не зарегистрирован. Пожалуйста, зарегистрируйся сначала.')


@dp.message_handler(Command('get_tasks'))  # /get_tasks
async def get_tasks(message: types.Message):
    telegram_id = str(message.from_user.id)

    try:
        user = await sync_to_async(ToDoListUser.objects.get)(telegram_id=telegram_id)
        tasks = await sync_to_async(list)(Task.objects.filter(user=user.id))
        await message.answer("Ваши задачи:\n")
        for task in tasks:
            await message.answer(f'Название: {task.title}\nОписание: {task.description}\n')

    except ToDoListUser.DoesNotExist:
        await message.answer('Ты не зарегистрирован. Пожалуйста, зарегистрируйся сначала.')

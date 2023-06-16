from aiogram.dispatcher.filters.state import StatesGroup, State


# В этом классе храним данные,
# а также состояния в котором находиться пользователь
class create_task(StatesGroup):
    test1 = State()
    test2 = State()

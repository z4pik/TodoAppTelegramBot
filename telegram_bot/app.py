import sqlite3


async def on_startup(dp):  # Создаём асинхронную функцию, которая будет запускаться по запуску бота

    import filters
    filters.setup(dp)

    # Создаём подключение к БД
    print('Подключение к SQLite')

    # Подключаемся к базе данных SQLite
    conn = sqlite3.connect('../db.sqlite3')
    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()

    # Пример выполнения SQL-запроса
    cursor.execute('SELECT * FROM todo_app_task')

    # Получаем результаты запроса
    results = cursor.fetchall()

    print("Бот запущен")


# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

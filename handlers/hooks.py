import sys
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook, start_polling

# Добавляем путь к директории проекта в sys.path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from utils.filters import register_all_commands
import logger
from config import *

async def on_startup(dp: Dispatcher):
    logger.debug("Бот запускается... Пожалуйста, подождите!  ")

async def on_shutdown(dp: Dispatcher):
    logger.debug("Бот отключается... Пожалуйста, подождите!  ")

if __name__ == '__main__':
    """
    Использование on_startup и on_shutdown:

    start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=False)
    """

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)
    
    # Регистрация всех команд, колбэков и инлайн-запросов из handlers/private
    register_all_commands(dp)
    start_polling(dp, skip_updates=False)

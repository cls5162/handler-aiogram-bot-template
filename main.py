import os
import importlib
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Автоматическая регистрация всех модулей из папки cogs
def register_all_commands(dp: Dispatcher):
    cogs_directory = './cogs'

    for filename in os.listdir(cogs_directory):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Удаляем '.py'
            module = importlib.import_module(f'cogs.{module_name}')
            if hasattr(module, 'register_commands'):
                module.register_commands(dp)

# Регистрация всех команд из cogs
register_all_commands(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

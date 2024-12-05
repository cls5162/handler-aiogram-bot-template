import os
import importlib
from aiogram import Dispatcher

def register_all_commands(dp: Dispatcher):

    handlers_directory = './handlers/private'

    for filename in os.listdir(handlers_directory):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Удаляем '.py'
            module = importlib.import_module(f'handlers.private.{module_name}')
            if hasattr(module, 'register_commands'):
                module.register_commands(dp)
            if hasattr(module, 'register_callback_queries'):
                module.register_callback_queries(dp)
            if hasattr(module, 'register_inline_queries'):
                module.register_inline_queries(dp)

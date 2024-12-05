import random
import time
import json
import os
from aiogram import Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

# Декоратор для регистрации обработчиков колбэков
def callback_query(callback_data: str):
    def decorator(func):
        func.callback_data = callback_data
        return func
    return decorator

def register_callback_queries(dp: Dispatcher):
    handlers = [func for func in globals().values() if hasattr(func, 'callback_data')]
    for handler in handlers:
        dp.register_callback_query_handler(handler, text=handler.callback_data)
import random
import time
import json
import os
from aiogram import Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

# Декоратор для регистрации обработчиков инлайн-запросов
def inline_query(inline_query_name: str):
    def decorator(func):
        func.inline_query_name = inline_query_name
        return func
    return decorator

def register_inline_queries(dp: Dispatcher):
    handlers = [func for func in globals().values() if hasattr(func, 'inline_query_name')]
    for handler in handlers:
        dp.register_inline_query_handler(handler, text=handler.inline_query_name)
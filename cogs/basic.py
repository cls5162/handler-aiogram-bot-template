import random
import time
import json
import os
from config import NAME_BOT
from aiogram import Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

# Декоратор для регистрации команд
def command(command_name: str):
    def decorator(func):
        func.command_name = command_name
        return func
    return decorator

@command("tech")
async def lawsuits_command(message: types.Message):
    args = message.text.split(maxsplit=1)  # Разделяем на команду и аргументы
    if len(args) < 2 or not args[1]:  # Проверка наличия второго аргумента и его валидности
        await message.answer("💙 Верная форма команды: /tech [Суть обращения]", parse_mode="HTML")
        return

    tech_ask = args[1]  # Суть обращения

    final_message = (
        f"🚀 Ваше обращение технической администрации успешно отправлено!\n\n"
        f"✉ Ваше обращение: {tech_ask}\n"
        f'👀 Ваш ID: {message.from_user.id}'
    )

    await message.answer(final_message, parse_mode="HTML")

def register_commands(dp: Dispatcher):
    handlers = [func for func in globals().values() if hasattr(func, 'command_name')]
    for handler in handlers:
        dp.register_message_handler(handler, commands=[handler.command_name])
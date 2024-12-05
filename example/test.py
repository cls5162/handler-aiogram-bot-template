import os
import sys

# Добавляем путь к директории проекта в sys.path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from database.tomato import Database

# Создаем базу данных
db = Database('database.json')

# Получаем значение по ключу
value = db.get('key')

# Устанавливаем значение по ключу
db.set('key', 'value')

# Удаляем значение по ключу
db.delete('key')

import time
import os
import sys
import logging

# Добавляем путь к директории проекта в sys.path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from config import *

# Настройка базового логгера
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s: logging/%(name)s]: %(message)s',
    handlers=[
        logging.FileHandler(LOGGING_CONF_FILE),
        logging.StreamHandler()
    ]
)

def debug(msg: str, file_name: str = None):
    logging.debug(msg, extra={'file_name': file_name})

def warning(msg: str, file_name: str = None):
    logging.warning(msg, extra={'file_name': file_name})

def info(msg: str, file_name: str = None):
    logging.info(msg, extra={'file_name': file_name})

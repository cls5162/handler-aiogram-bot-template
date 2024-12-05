import json
import os
from config import DB_APPLY
import logger

class Database:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data = {}
        self.enabled = DB_APPLY
        if self.enabled:
            self.load()
        else:
            logger.warning("БазаДанных не может быть подвергнута использованию, т.к. выключена в config.py!")

    def load(self):
        if os.path.exists(self.file_name) and self.enabled:
            with open(self.file_name, 'r') as f:
                self.data = json.load(f)

    def save(self):
        if self.enabled:
            with open(self.file_name, 'w') as f:
                json.dump(self.data, f)

    def get(self, key: str, default=None):
        if self.enabled:
            return self.data.get(key, default)

    def set(self, key: str, value):
        if self.enabled:
            self.data[key] = value
            self.save()

    def delete(self, key: str):
        if self.enabled and key in self.data:
            del self.data[key]
            self.save()

import os
import hashlib
import logging
from Config.config_file import local_file
from files_func.get_files import get_files
from typing import Dict


def get_files_size() -> dict:
    """Функция создания словаря из файлов локальной папки, где ключи - имя файла, значения - хэш-суммы файлов. Если
    папки нет,  выдает исключение FileNotFoundError
    return: dict - словарь из файдлв локальной папки"""
    try:
        files = get_files()
        files_hash: Dict = {}
        for file in files:
            with open(os.path.join(local_file, file), 'rb') as data:
                text = data.read()
                files_hash[file] = hashlib.sha256(text).hexdigest()
        return files_hash
    except FileNotFoundError:
        logging.error('не удалось найти папку')

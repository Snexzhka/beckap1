import logging
import os
from Config.config_file import local_file


def get_files() -> list:
    """Функция получения списка файлов в локальной папке. Формирует список из файлов в заданной директории. При
    невозможности найти файл выдает исключение FileNotFoundError и завершает работу
    return: list - список файлов в папке"""
    try:
        logging.info('начинаю делать лист')
        return os.listdir(local_file)

    except FileNotFoundError:
        logging.error('Невозможно найти папку')
        exit()

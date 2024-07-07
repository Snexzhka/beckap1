import logging
from requests.exceptions import ConnectionError
from time import sleep
from files_func.get_files_size import get_files_size
from API.get_file import get_file
from executive_functions.comprassion_files import comprassion_files
from executive_functions.files_update import files_update
from executive_functions.files_delete import files_delete
from typing import Dict


def function(num: int) -> None:
    """Основная функция для управления функциями добавления, обновления и удаления файлов из облака. На вход получает
    интервал времени в секундах , через который происходит сравнение файловю При невозможности подключиться к облаку
    выдает исключение ConnectionRefusedError
    param num: int - интервал времени в секундах"""
    try:
        cloud_storage: Dict = get_file()
        local_storage: Dict = get_files_size()
        if cloud_storage == 404:
            logging.error('невозможно получить данные из облака')
            raise ConnectionRefusedError
        comprassion_files(cloud_storage, local_storage)
        files_update(cloud_storage, local_storage)
        files_delete(cloud_storage, local_storage)
    except ConnectionError:
        logging.error('нет соединения')
    except ConnectionRefusedError:
        logging.error('невозможно получить данные из облака')

    sleep(num)

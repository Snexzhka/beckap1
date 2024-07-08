import logging
import requests
from API.take_url import take_url
from typing import Dict


def reload(path: str, file: str) -> int | None:
    """Функция записи файла в облачное хранилище, если файла там нет. Получает ссылку на загрузку файла в облако.
     При невозможности возвращает код 404. Открывает файл в бинарном режиме и формирует словарь для передачи в
     облако. Если открыть файл не удалось, возвращает исключение FileNotFoundError и код 410. При удачном результате
     работы возвращает статус запроса.
     param path: str - путь в файлу в локальной папке
     param file: str - файл в локальной папке для передачи в облако
     param mode: bool - режим перезаписи
     return: int| None - статус запроса или ошибка
    """
    url: str = take_url(file, mode=True)
    if url == 404:
        logging.error('не удалось получить ссылку')
        return 404
    try:
        fileload = open(path, 'rb')
    except FileNotFoundError:
        logging.error(f'невозможно открыть файл {file}')
        return
    files: Dict = {'file': fileload}
    response = requests.post(url, files=files)
    fileload.close()
    return response.status_code

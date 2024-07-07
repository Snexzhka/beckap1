import requests
import logging
from API.take_url import take_url
from typing import Dict


def load_file(path: str, file: str) -> int:
    """Функция записи файла в облачное хранилище, если файл в локальной папке изменен. Получает ссылку для загрузки
    файла на яндекс диск. Открывает файл в бинарном режиме,формирует словарь для передачи в качестве аргумента в API
    запрос. При успешной работе возвращет статус запроса. При невозможности прочтения файла возвращает исключение
    FileNotFoundError и код 410. При невозможности получить ссылку для загрузки возвращает код 404.
    param: path: str - путь к файлу в локальной папке
    param file: str -  файл для загрузки (измененный файл)
    return: int - статус запроса"""
    url: str = take_url(file)
    if url == 404:
        logging.error('не удалось получить ссылку')
        return 404
    try:
        files_load = open(path, 'rb')
    except FileNotFoundError:
        logging.error('невозможно открыть файл')
        return 410
    files: Dict = {'file': files_load}
    response = requests.post(url, files=files)
    files_load.close()
    logging.info('файл успешно загружен в облако')
    return response.status_code

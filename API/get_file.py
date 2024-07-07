import logging
import requests
import time
from Config.config_file import TOKEN, disk_path
from typing import Dict

url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def get_file() -> dict | int:
    """Функция создания словаря из файлов папки в облаке,  ключами являются названия файлов, значениями - хэш-суммы.
    Функция возвращает словарь при успешном результате работы либо код 404.
    return: dict| int  - статус запроса или 404"""
    response = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources?path={disk_path}', headers=headers)
    response = response.json()
    if response.get('_embedded'):
        data: Dict = {}
        data_response: Dict = response['_embedded']['items']
        for files in data_response:
            data[files['name']] = files['sha256']
        logging.info('словарь успешно создан')
        return data
    else:
        logging.error('ошибка соединения')
        time.sleep(3)
        return 404

import requests
import time
from Config.config_file import TOKEN, disk_path
from typing import Dict


def get_file() -> dict | int:
    """Функция создания словаря из файлов папки в облаке,  ключами являются названия файлов, значениями - хэш-суммы.
    Функция возвращает словарь при успешном результате работы либо код 404.
    return: dict| int  - статус запроса или 404"""
    response = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources?path={disk_path}',
                            headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                     'Authorization': f'OAuth {TOKEN}'})
    response = response.json()
    if response.get('_embedded'):
        data: Dict = {}
        data_response: Dict = response['_embedded']['items']
        for file in data_response:
            data[file['name']] = file['sha256']
        return data
    else:
        time.sleep(3)
        return 404

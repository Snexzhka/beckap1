import os.path
import requests
import logging
from Config.config_file import TOKEN, disk_path


url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_a_folder() -> None:
    """Функция для создания папки на янлдекс диске. Если папка есть, функция завершает работу."""
    if not os.path.isdir(disk_path):
        requests.put(f'{url}?path={disk_path}', headers=headers)
        logging.info('Папка на диске создана ')
    else:
        logging.info('Папка на диске существует ')
        return

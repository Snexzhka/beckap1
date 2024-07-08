import requests
import logging
from Config.config_file import disk_path
from API.params import url, headers


def create_a_folder() -> None:
    """Функция для создания папки на янлдекс диске. Если папка есть, функция завершает работу."""
    response = requests.put(f'{url}?path={disk_path}', headers=headers)
    if response == 201:
        logging.info(f'Папка {disk_path} на диске создана ')
    elif response == 401:
        logging.error(f'Папка {disk_path} не создана, пользователь не авторизован.')
    elif response == 403:
        logging.error(f'API недоступно. Слишком много файлов')
    elif response == 423:
        logging.error(f'Техработы сайтаю Папка {disk_path} не создана')
    else:
        logging.info(f'Папка {disk_path} на диске уже существует ')

import requests
from Config.config_file import TOKEN, disk_path


def take_url(file: str, mode=False) -> str | int:
    """Функция получения ссылки для загрузки файла в облачное хранилице. Отправляет API запрос, возвращает ссылку
    для загрузки файла. При невозможности получения ссылки возвращает код 404.
    param file: str - файл для загрузки в облако
    param mode: bool - режим перезаписи
    return str|int - ссылка или ошибка"""
    response = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={disk_path}/{file}'
                            f'&overwrite={mode}', headers={'Accept': 'application/json', 'Authorization': TOKEN}).json()
    if response.get('href'):
        return response['href']
    else:
        return 404

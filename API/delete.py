import requests
from Config.config_file import TOKEN, disk_path

url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def delete(file: str) -> int:
    """Функция удаления файла с яндекс диска, если его уже нет в папке в локальном хранилище. Возвращает результат
    работы в виде статуса API запроса к яндекс диску
    param file: str - файл в локальном хранилище
    return: int - статус запроса """
    response = requests.delete(f'https://cloud-api.yandex.net/v1/disk/resources?path={disk_path}/{file}',
                               headers=headers)
    return response.status_code

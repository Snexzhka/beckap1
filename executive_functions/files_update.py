import logging
import os
from Config.config_file import local_file
from API.load import load_file


def files_update(cloud_storage: dict, local_storage: dict) -> None:
    """Функция добавления  файлов в облако при их появлении в локальной папке. Получает на вход два словаря, содержащих
    имя файла (ключ словаря) и хэш_сумма (значение) - в локальнойм хранилище и в облаке. Если в облаке отстутвует такой
    ключ словаря, как в локальной папке, файл записывается в облако. При отсутствии интернета,выдает исключение
    ConnectionError.
    param cloud_storage: dict - словарь из файлов папки в облаке
    param local_storage: dict - словарь из файлов локальной папки.
    """
    if cloud_storage.keys() == local_storage.keys():
        return
    for file in local_storage.keys():
        try:
            if not cloud_storage.get(file):
                response = load_file(os.path.join(local_file, file), file)
                if response == 201:
                    logging.info(f'файл {file} успешно записан')
                elif response == 507:
                    logging.error(f'файл {file} не записан, Недостаточно места')
                elif response == 413:
                    logging.error(f'Файл {file} слишком большой. Не удалось записать файл {file}')
                elif response == 423:
                    logging.error(f'На сайте технические работы. Не удалось записать файл {file}')
                elif response == 503:
                    logging.error(f'Сервис временно недоступен. файл {file} не загружен.')
                else:
                    logging.error(f'не удалось записать файл {file}')
        except ConnectionError:
            logging.error('ошибка соединения')

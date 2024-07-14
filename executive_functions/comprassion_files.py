import logging
import os
from Config.config_file import local_file
from API.reload import reload


def comprassion_files(cloud_storage: dict, local_storage: dict) -> None:
    """Функция для дозаписи файла, если файл в локальной папке изменен. Получает на вход два словаря, содержащих имя
    файла (ключ словаря) и хэш_сумма (значение) - в локальнойм хранилище и в облаке. Если ключи равны, а значения нет,
    дозаписывает файл в облако. При невозможности получить папку из облака возвращает исключение ConnectionRefusedError.
    param cloud_storage: dict - словарь из файлов папки в облаке
    param local_storage: dict - словарь из файлов локальной папки.
    """

    for file in local_storage.keys():
        if cloud_storage.get(file):
            if cloud_storage[file] != local_storage[file]:
                response = reload(os.path.join(local_file, file), file)
                if response == 201:
                    logging.info(f'файл {file} успешно изменен')
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

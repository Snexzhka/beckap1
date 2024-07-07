import logging
import os
from Config.config_file import local_file
from API.load import load_file


def files_update(cloud_storage: dict, local_storage: dict) -> None:
    """Функция добавления  файлов в облако при их появлении в локальной папке. Получает на вход два словаря, содержащих
    имя файла (ключ словаря) и хэш_сумма (значение) - в локальнойм хранилище и в облаке. Если в облаке отстутвует такой
    ключ словаря, как в локальной папке, файл записывается в облако. При невозможности получть словарь из облака,
    выдает исключение ConnectionError.
    param cloud_storage: dict - словарь из файлов папки в облаке
    param local_storage: dict - словарь из файлов локальной папки.
    """
    for file in local_storage.keys():
        try:
            if not cloud_storage.get(file):
                response = load_file(os.path.join(local_file, file), file)
                if response == 201:
                    logging.info('файл успешно записан')
                else:
                    logging.error('не удалось записать файл')
        except ConnectionError:
            logging.error('ошибка соединения')

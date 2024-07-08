import logging
from API.delete import delete


def files_delete(cloud_storage: dict, local_storage: dict) -> None:
    """Функция удаления файла в облаке, если он удален в локальной папке. Получает на вход два словаря, содержащих имя
    файла (ключ словаря) и хэш_сумма (значение) - в локальнойм хранилище и в облаке. Сравнивает ключи словарей, и если
    в локальной хранилище больше нет такого ключа, как в облаке, удаляет файл из облака. При успешном удалении
    записывает сообщения в лог. Если отсутствует интернет, выдает исключение ConnectionError.
    param cloud_storage: dict - словарь из файлов папки в облаке
    param local_storage: dict - словарь из файлов локальной папки.
    """
    if cloud_storage.keys() == local_storage.keys():
        return
    for file in cloud_storage.keys():
        if not local_storage.get(file):
            response = delete(file)
            if response == 204:
                logging.info(f'файл {file} успешно удален')
            elif response == 423:
                logging.error(f'Файл {file} не удален. Технические работы')
            elif response == 503:
                logging.error(f'Файл {file} не удален.Сервис временно недоступен.')
            else:
                logging.error(f'не удалось удалить  файл {file}, нет соединения')

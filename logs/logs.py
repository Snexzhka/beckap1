import logging


def logs_message() -> logging:
    """Функция создания файла логирования и сообщений для этого файла"""

    logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s - %(name)s', encoding='utf8')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(f'{__name__}.log', mode='w', encoding='utf8')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s %(name)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(f"тестируем программу {__name__}")
    return logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w',
                               format='%(asctime)s - %(levelname)s - %(message)s - %(name)s', encoding='utf8')
